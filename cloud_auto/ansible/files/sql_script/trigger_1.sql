CREATE OR REPLACE TRIGGER IMPADMIN.INSERT_TO_PHYSICAL_TB
BEFORE INSERT ON IMPADMIN.IMAGE

FOR EACH ROW

DECLARE
	newimageId NUMBER;
	newimageUuid VARCHAR(32);
	newupdaterUuid VARCHAR(32);
	newproductName VARCHAR(1024);
	newproductVersion VARCHAR(1024);
	newimageFrom VARCHAR(32);
	newisSnapshot VARCHAR(2);

BEGIN
SELECT :new.imageId INTO newimageId FROM Dual;
SELECT :new.imageuuid INTO newimageUuid FROM Dual;
SELECT :new.productname INTO newproductName FROM Dual;
SELECT :new.productversion INTO newproductVersion FROM Dual;
SELECT :new.imagefrom INTO newimageFrom FROM Dual;
SELECT :new.issnapshot INTO newisSnapshot FROM Dual;
SELECT :new.updaterUuid INTO newupdaterUuid FROM Dual;

IF (newupdaterUuid = 'Identifier') THEN
	INSERT INTO IMPADMIN.PHYSICALIMAGE
	   	   (imageId, imageuuid, productname,
			productversion, imagefrom, issnapshot)
	VALUES (newimageId, newimageUuid, newproductName,
	        newproductVersion, newimageFrom, newisSnapshot);
END IF;
EXCEPTION
	WHEN DUP_VAL_ON_INDEX THEN
		DBMS_OUTPUT.PUT_LINE('I DONT KNOW. WHY DUP');
END;
