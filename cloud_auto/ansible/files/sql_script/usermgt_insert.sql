insert into "USERMGT"."PROJECT" ("ID", "NAME", "DESCRIPTION", "CREATEDTIME", "UPDATEDTIME", "DELETEDTIME", "ISDELETED", "TENANTID", "UUID", "SUPERPROJECTID" ) values (29272193, 'CSP', 'For CSP', SYSTIMESTAMP, SYSTIMESTAMP, null, '0', 121236589, '01bea881', 752141285);

insert into "USERMGT"."TENANT" ("ID", "NAME", "CREATEDTIME", "UPDATEDTIME", "DELETEDTIME", "DESCRIPTION", "ISDELETED", "UUID", "OWNER", "CREATOR" ) values (121236589, 'CSP', SYSTIMESTAMP, SYSTIMESTAMP, null, 'For CSP', '0', '0739ec6d', 699103620, 'csp@tmax.co.kr');

insert into "USERMGT"."USERS" ("ID", "EMAIL", "NAME", "POSITION", "DEPARTMENT", "COMPANYID", "PHONE", "PAYMENTID", "CREATEDTIME", "UPDATEDTIME", "DELETEDTIME", "ISDELETED", "UUID", "TENANTID", "UTYPE", "COMPANY", "PAYMENT" ) values (102416560, 'csp@tmax.co.kr', 'CSP Admin', null, null, null, null, null, SYSTIMESTAMP, SYSTIMESTAMP, null, '0', '061ac0b0', 0, 'csp', null, null);

commit;
exit
