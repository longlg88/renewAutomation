INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, ipValue, vlanId, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime) VALUES(100000001, '5F5E101', 0, '192.169.100.57', 'none', 100000001, 3232326713, -1, 100000001, '5F5E101', 'none', 'Active', 'F', NULL, NULL, SYSTIMESTAMP);
INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, ipValue, vlanId, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime) VALUES(100000002, '5F5E102', 0, '192.169.100.58', 'none', 100000001, 3232326714, -1, 100000001, '5F5E102', 'none', 'Active', 'F', NULL, NULL, SYSTIMESTAMP);
INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, ipValue, vlanId, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime) VALUES(100000003, '5F5E103', 0, '192.169.100.59', 'none', 100000001, 3232326715, -1, 100000001, '5F5E103', 'none', 'Active', 'F', NULL, NULL, SYSTIMESTAMP);
INSERT INTO PUBLICIPINFO(publicIp, publicIpId, publicIpUuid, vportId, createdTime) VALUES('192.169.100.22', 100000001, '5F5E101', 100000001, SYSTIMESTAMP);
commit;
exit;
INSERT INTO PUBLICIPINFO(publicIp, publicIpId, publicIpUuid, vportId, createdTime) VALUES('192.169.100.23', 100000002, '5F5E102', 100000002, SYSTIMESTAMP);
commit;
exit;
INSERT INTO PUBLICIPINFO(publicIp, publicIpId, publicIpUuid, vportId, createdTime) VALUES('192.169.100.24', 100000003, '5F5E103', 100000003, SYSTIMESTAMP);
commit;
exit;