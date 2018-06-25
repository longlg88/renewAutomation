
DROP TABLE CSVM_FILE_STALE;
DROP TABLE CSVM_FILE_DIV;
DROP TABLE CSVM_SSVR;
DROP TABLE CSVM_FILE;
DROP TABLE CSVM_DB;
DROP TABLE CSVM_SSVR_GROUP;
DROP TABLE CSVM_STORAGE;
DROP TABLE CSVM_STORAGE_GROUP;
DROP TABLE CSVM_TENANT;

DROP SEQUENCE CSVM_FILE_SEQ;
DROP SEQUENCE CSVM_SSVR_SEQ;

CREATE SEQUENCE CSVM_FILE_SEQ;
CREATE SEQUENCE CSVM_SSVR_SEQ;

CREATE TABLE CSVM_TENANT
(
    TENANT_UUID         VARCHAR2(8),
    TENANT_NAME         VARCHAR2(64),
    QUOTA               NUMBER,
    CONSTRAINT CSVM_TENANT_PK PRIMARY KEY (TENANT_UUID)
);

CREATE TABLE CSVM_STORAGE_GROUP
(
    STORAGE_GROUP_UUID      VARCHAR2(8),
    CONSTRAINT CSVM_STORAGE_GROUP_PK PRIMARY KEY(STORAGE_GROUP_UUID)
);

CREATE TABLE CSVM_STORAGE
(
    STORAGE_ID              NUMBER,
    STORAGE_UUID            VARCHAR2(8),
    STORAGE_TYPE            NUMBER,
    TOTAL_SIZE              NUMBER,
    STORAGE_GROUP_UUID      VARCHAR2(8),
    CONSTRAINT CSVM_STORAGE_PK PRIMARY KEY(STORAGE_ID),
    CONSTRAINT CSVM_STORAGE_FK FOREIGN KEY(STORAGE_GROUP_UUID)
        REFERENCES CSVM_STORAGE_GROUP(STORAGE_GROUP_UUID)
);

CREATE TABLE CSVM_SSVR_GROUP
(
    SSVR_GROUP_UUID         VARCHAR2(8),
    STORAGE_GROUP_UUID      VARCHAR2(8),
    CONSTRAINT CSVM_SSVR_GROUP_PK PRIMARY KEY(SSVR_GROUP_UUID),
    CONSTRAINT CSVM_SSVR_GROUP_FK FOREIGN KEY(STORAGE_GROUP_UUID)
        REFERENCES CSVM_STORAGE_GROUP (STORAGE_GROUP_UUID)
);

CREATE TABLE CSVM_DB
(
    TENANT_UUID             VARCHAR2(8),
    DB_UUID                 VARCHAR2(8),
    SSVR_GROUP_UUID         VARCHAR2(8),
    QUOTA                   NUMBER,
    CONSTRAINT CSVM_DB_PK PRIMARY KEY (DB_UUID),
    CONSTRAINT CSVM_DB_FK FOREIGN KEY (SSVR_GROUP_UUID)
        REFERENCES CSVM_SSVR_GROUP (SSVR_GROUP_UUID),
    CONSTRAINT CSVM_DB_FK_TENANT FOREIGN KEY (TENANT_UUID)
        REFERENCES CSVM_TENANT (TENANT_UUID)
);

CREATE TABLE CSVM_FILE
(
    FILE_ID         NUMBER, 
    FILE_NAME       VARCHAR2(256), 
    FILE_SIZE       NUMBER,
    DB_UUID         VARCHAR2(8),
    STRIPING_SIZE   NUMBER,
    DIV_COUNT       NUMBER,
    REDUN_COUNT     NUMBER,
    CONSTRAINT CSVM_FILE_PK PRIMARY KEY (FILE_ID),
    CONSTRAINT CSVM_FILE_FK FOREIGN KEY (DB_UUID)
        REFERENCES CSVM_DB (DB_UUID),
    CONSTRAINT CSVM_FILE_UQ UNIQUE (DB_UUID, FILE_NAME)
);

CREATE TABLE CSVM_SSVR
(
    SSVR_ID                 NUMBER,
    SSVR_UUID               VARCHAR2(8),
    STORAGE_ID              NUMBER,
    STORAGE_UUID            VARCHAR2(8),
    SSVR_IP               VARCHAR2(40),
    SSVR_PORT             NUMBER,
    SSVR_GROUP_UUID         VARCHAR2(8),
    INVALID_FLAG            NUMBER(1,0) DEFAULT 1,
    INCARNATION_NUM         NUMBER,
    SSVR_TYPE               NUMBER DEFAULT 2,
    CONSTRAINT CSVM_SSVR_PK PRIMARY KEY (SSVR_ID),
    CONSTRAINT CSVM_SSVR_STORAGE_FK FOREIGN KEY (STORAGE_ID)
        REFERENCES CSVM_STORAGE (STORAGE_ID),
    CONSTRAINT CSVM_SSVR_FK FOREIGN KEY (SSVR_GROUP_UUID)
        REFERENCES CSVM_SSVR_GROUP (SSVR_GROUP_UUID)
);

CREATE TABLE CSVM_FILE_DIV
(
    FILE_ID                 NUMBER,
    DIV_NUM                 NUMBER,
    REDUN_NUM               NUMBER,
    FILE_DIV_SIZE           NUMBER,
    SSVR_ID                 NUMBER,
    FILE_DIV_PATH           VARCHAR2(256),
    STATE                   NUMBER(1,0) DEFAULT 0,
    CONSTRAINT CSVM_FILE_DIV_PK PRIMARY KEY (FILE_ID, DIV_NUM, REDUN_NUM, STATE),
    CONSTRAINT CSVM_FILE_DIV_FK FOREIGN KEY (FILE_ID)
        REFERENCES CSVM_FILE (FILE_ID),
    CONSTRAINT CSVM_FILE_DIV_SSVR_FK FOREIGN KEY (SSVR_ID)
        REFERENCES CSVM_SSVR (SSVR_ID)
);

CREATE TABLE CSVM_FILE_STALE
(
    FILE_ID                 NUMBER,
    REDUN_NUM               NUMBER,
    DIV_NUM                 NUMBER,
    STRIPENO                NUMBER,
    SSVR_ID                 NUMBER,
    STATE                   NUMBER(1,0) DEFAULT 0,
    CONSTRAINT CSVM_FILE_STALE_PK PRIMARY KEY(FILE_ID, REDUN_NUM, STRIPENO, STATE),
    CONSTRAINT CSVM_FILE_STALE_FK FOREIGN KEY(FILE_ID)
        REFERENCES CSVM_FILE (FILE_ID),
    CONSTRAINT CSVM_FILE_STALE_SSVR_FK FOREIGN KEY (SSVR_ID)
        REFERENCES CSVM_SSVR (SSVR_ID)
);

CREATE OR REPLACE VIEW CSVM_DB_STORAGE_USAGE
AS
SELECT F.DB_UUID, F.DB_SIZE, DB.QUOTA
FROM
(
    SELECT DB_UUID, SUM(FILE_SIZE) DB_SIZE
    FROM CSVM_FILE
    GROUP BY DB_UUID
) F, CSVM_DB DB
WHERE DB.DB_UUID = F.DB_UUID;

CREATE OR REPLACE VIEW CSVM_TENANT_STORAGE_USAGE
AS
SELECT T.TENANT_UUID, T.TENANT_NAME, T.QUOTA, A.TOTAL_SIZE 
FROM
(
    SELECT TENANT_UUID, SUM(DB_SIZE) TOTAL_SIZE
    FROM 
    (
        SELECT DB.TENANT_UUID, F.DB_UUID, F.DB_SIZE, DB.QUOTA
        FROM
        (
            SELECT DB_UUID, SUM(FILE_SIZE) DB_SIZE
            FROM CSVM_FILE
            GROUP BY DB_UUID
        ) F, CSVM_DB DB
        WHERE DB.DB_UUID = F.DB_UUID
    )
    GROUP BY TENANT_UUID
) A, CSVM_TENANT T
WHERE T.TENANT_UUID = A.TENANT_UUID;

COMMIT;