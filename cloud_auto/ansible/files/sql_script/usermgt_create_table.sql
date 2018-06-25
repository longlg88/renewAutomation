CREATE TABLE PORTAL.PROJECT (
	ID NUMBER,
	NAME VARCHAR(255),
	DESCRIPTION VARCHAR(255),
	CREATEDTIME TIMESTAMP,
	UPDATEDTIME TIMESTAMP,
	DELETEDTIME TIMESTAMP,
	ISDELETED CHAR(1),
	TENANTID NUMBER,
	UUID VARCHAR(255),
	SUPERPROJECTID NUMBER
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


GRANT SELECT ON PORTAL.PROJECT TO AUTH;

CREATE TABLE PORTAL.PROJECT_USER_RELATION (
	PROJECTID NUMBER,
	USERID NUMBER,
	ROLEID NUMBER
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


GRANT SELECT ON PORTAL.PROJECT_USER_RELATION TO AUTH;

CREATE TABLE PORTAL.RESOURCE_QUOTA (
	OBJECTID NUMBER NOT NULL,
	NAME VARCHAR(255) NOT NULL,
	VALUE NUMBER,
	UNIT VARCHAR(255),
	OBJECT_TYPE VARCHAR(31)
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

CREATE UNIQUE INDEX PORTAL.PORTAL_CON121400739 ON PORTAL.RESOURCE_QUOTA (
	OBJECTID ASC,
	NAME ASC
)
LOGGING
TABLESPACE USR
PCTFREE 10
INITRANS 2;

ALTER TABLE PORTAL.RESOURCE_QUOTA ADD 
PRIMARY KEY (
	OBJECTID,
	NAME
);


GRANT SELECT ON PORTAL.RESOURCE_QUOTA TO AUTH;

CREATE TABLE PORTAL.SERVICE (
	ID NUMBER,
	UUID VARCHAR(255),
	NAME VARCHAR(255),
	DESCRIPTION VARCHAR(255),
	CREATEDTIME DATE,
	UPDATEDTIME DATE,
	DELETEDTIME DATE,
	ISDELETED CHAR(1)
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


GRANT SELECT ON PORTAL.SERVICE TO AUTH;

CREATE TABLE PORTAL.TENANT (
	ID NUMBER,
	NAME VARCHAR(255),
	CREATEDTIME TIMESTAMP,
	UPDATEDTIME TIMESTAMP,
	DELETEDTIME TIMESTAMP,
	DESCRIPTION VARCHAR(255),
	ISDELETED CHAR(1),
	UUID VARCHAR(255),
	OWNER NUMBER,
	CREATOR VARCHAR(255)
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;


GRANT SELECT ON PORTAL.TENANT TO AUTH;

CREATE TABLE PORTAL.USERS (
	ID NUMBER,
	EMAIL VARCHAR(255) NOT NULL,
	NAME VARCHAR(255),
	POSITION VARCHAR(255),
	DEPARTMENT VARCHAR(255),
	COMPANYID NUMBER,
	PHONE VARCHAR(255),
	PAYMENTID NUMBER,
	CREATEDTIME TIMESTAMP,
	UPDATEDTIME TIMESTAMP,
	DELETEDTIME TIMESTAMP,
	ISDELETED CHAR(1),
	UUID VARCHAR(255),
	TENANTID NUMBER,
	UTYPE VARCHAR(30),
	COMPANY VARCHAR(255),
	PAYMENT VARCHAR(255),
	ROLE VARCHAR(255),
	DESCRIPTION VARCHAR(255)
)
TABLESPACE USR
PCTFREE 10
INITRANS 2
STORAGE (
	MAXEXTENTS UNLIMITED
)
LOGGING
NOPARALLEL;

CREATE UNIQUE INDEX PORTAL.PORTAL_CON246500095 ON PORTAL.USERS (
	EMAIL ASC
)
LOGGING
TABLESPACE USR
PCTFREE 10
INITRANS 2;

ALTER TABLE PORTAL.USERS ADD 
PRIMARY KEY (
	EMAIL
);


GRANT SELECT ON PORTAL.USERS TO AUTH;
