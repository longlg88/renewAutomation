insert into "AUTH"."SM_ISSUER" ("IS_NAME", "IS_TYPE", "IS_SECRET", "IS_ID_ENC", "IS_RBAC_M" ) values ('portal', 'HMAC_256', 'sys', 0, 0);

insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('888541943', 'comm', null, 'SERVICE_EXECUTE', 'imp.master.InstancesList', null);
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('716234885', 'csp', 'csp', 'read', 'csp', 'csp');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('871192648', 'csp', 'csp', 'admin', 'csp', 'csp');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('659728649', 'storage', null, 'create', 'storage', 'storage');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('482671967', 'storage', null, 'read', 'storage', 'storage');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('490641218', 'storage', null, 'update', 'storage', 'storage');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('729958254', 'storage', null, 'delete', 'storage', 'storage');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('249623599', 'host', null, 'create', 'host', 'host');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('444537875', 'host', null, 'update', 'host', 'host');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('124947627', 'host', null, 'delete', 'host', 'host');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('418156577', 'host', null, 'read', 'host', 'host');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('628894340', 'comm', null, 'SERVICE_EXECUTE', 'imp.master.ImageListGet', null);
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('335942386', 'compute', null, 'read', 'compute', 'compute');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('433260917', 'compute', null, 'create', 'compute', 'compute');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('206104939', 'compute', null, 'update', 'compute', 'compute');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('603746321', 'compute', null, 'delete', 'compute', 'compute');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('796817243', 'image', null, 'create', 'image', 'image');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('340444697', 'image', null, 'read', 'image', 'image');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('768467502', 'image', null, 'update', 'image', 'image');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('261141658', 'image', null, 'delete', 'image', 'image');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('615542588', 'network', null, 'create', 'network', 'network');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('777171178', 'network', null, 'read', 'network', 'network');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('138317939', 'network', null, 'update', 'network', 'network');
insert into "AUTH"."SM_PERMISSION" ("ID", "OBJECT_TYPE", "OBJECT_ID", "ACTION", "OBJECT_SYS_ID", "OBJECT_NAME" ) values ('341072344', 'network', null, 'delete', 'network', 'network');

insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('06', null, 'csp', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('161502720', null, 'Admin', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('144822747', null, 'Compute Manager', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('514727618', null, 'Image Manager', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('102264507', null, 'Network Manager', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('623089023', null, 'Host Manager', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('520888133', null, 'Storage Manager', null, null, null);
insert into "AUTH"."SM_ROLE" ("ROLE_ID", "DESCRIPTION", "ROLE_NAME", "CARDINALITY", "PRE_ROLE_ID", "SET_ID" ) values ('606350719', null, 'General User', null, null, null);

insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '888541943');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '716234885');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '871192648');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('520888133', '659728649');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('520888133', '729958254');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('520888133', '482671967');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('520888133', '490641218');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('514727618', '796817243');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('514727618', '340444697');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('514727618', '768467502');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('514727618', '261141658');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '206104939');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '335942386');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '433260917');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '603746321');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '418156577');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '335942386');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '124947627');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '249623599');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('06', '444537875');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('144822747', '628894340');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('102264507', '138317939');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('102264507', '341072344');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('102264507', '615542588');
insert into "AUTH"."SM_ROLE_PERMISSION" ("ROLE_ID", "PERMISSION_ID" ) values ('102264507', '777171178');

insert into "AUTH"."SM_USER" ("USER_ID", "PASSWD" ) values ('csp@tmax.co.kr', 'n8gHHWIIvmB7djJSgVsnzA==');

insert into "AUTH"."SM_USER_ROLE" ("USER_ID", "ROLE_ID" ) values ('csp@tmax.co.kr', '06');

commit;
exit
