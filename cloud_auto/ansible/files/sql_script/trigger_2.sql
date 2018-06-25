CREATE OR REPLACE TRIGGER IMPADMIN.UPDATE_TO_IMAGE_TB 
BEFORE UPDATE ON IMPADMIN.PHYSICALIMAGE 

FOR EACH ROW

DECLARE
	newimageId NUMBER;	
	newuploadedTime TIMESTAMP;
	newupdatedTime TIMESTAMP;

BEGIN
SELECT :new.imageId INTO newimageId FROM Dual;
SELECT :new.importedTime INTO newuploadedTime FROM Dual;
SELECT :new.editedTime INTO newupdatedTime FROM Dual;


	UPDATE IMPADMIN.Image SET
	   	   imageId = newimageId, 
	   	   uploadedTime = newuploadedTime, 
	   	   updatedTime = newupdatedTime, 
		   updaterUuid = null		   
 	WHERE  imageId = newimageId;
END;
