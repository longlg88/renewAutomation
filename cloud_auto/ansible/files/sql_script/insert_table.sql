------- Begin of IMPADMIN.INSTANCESPECINFO-------

insert into "INSTANCESPECINFO" ("SPECID", "SPECUUID", "SPECTYPE", "SPECCPU", "SPECMEMORY" ) values (305992401, '123d12d1', 'small', 1, 256);
insert into "INSTANCESPECINFO" ("SPECID", "SPECUUID", "SPECTYPE", "SPECCPU", "SPECMEMORY" ) values (305805873, '123a3a31', 'medium', 1, 512);
insert into "INSTANCESPECINFO" ("SPECID", "SPECUUID", "SPECTYPE", "SPECCPU", "SPECMEMORY" ) values (305994298, '123d1a3a', 'large', 2, 2048);
insert into "INSTANCESPECINFO" ("SPECID", "SPECUUID", "SPECTYPE", "SPECCPU", "SPECMEMORY" ) values (996477619, '3b650ab3', 'x-small', 1, 128);
insert into "INSTANCESPECINFO" ("SPECID", "SPECUUID", "SPECTYPE", "SPECCPU", "SPECMEMORY" ) values (996477620, '3b650ab4', 'x-large', 2, 4096);

------- End of IMPADMIN.INSTANCESPECINFO -------

------- Begin of PHYSICALIMAGE -------

insert into physicalImage (imageid, imageuuid, productname, productversion) values (1234,'1234','productname','productversion');

------- End of PHYSICALIMAGE -------

commit;
exit;
