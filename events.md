Sample output

Results:
{
    "metaData": {
        "limit": 2048,
        "more": false
    },
    "data": [
        {
            "eventTime": "2025-01-07T16:03:46.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"38b0239a-f1f5-4d1b-9f4c-28b43a4258cc\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/215d80e5-5da5-47a7-a4bc-4403ff787ba2",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/38b0239a-f1f5-4d1b-9f4c-28b43a4258cc"
            }
        },
        {
            "eventTime": "2025-01-07T16:03:42.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"01d7f9ad-d0e4-421b-9cc2-f1193cecad33\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/1fcc9fe7-9bb2-40ce-a074-fa9091bc6a65",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T16:03:37.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"3b5040b0-c005-427c-8565-de8d8bf3fdc9\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/2ae0b2c1-2d27-4946-a662-ff0c6e6e5e34",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:02:45.000Z",
            "event": "EDGE_UP",
            "category": "EDGE",
            "severity": "INFO",
            "message": "Edge [branch1-vedge]  has re-established communication with the Orchestrator",
            "detail": "{\"enterpriseAlertConfigurationId\":null,\"enterpriseId\":1,\"edgeId\":4,\"edgeName\":\"branch1-vedge\",\"state\":\"PENDING\",\"stateSetTime\":\"2025-01-07T16:02:45.055Z\",\"triggerTime\":\"2025-01-07T16:02:45.055Z\",\"remainingNotifications\":1,\"nextNotificationTime\":\"2025-01-07T16:02:45.055Z\",\"lastContact\":\"2025-01-07T16:02:41.691Z\",\"name\":\"EDGE_UP\",\"type\":\"EDGE_UP\",\"firstNotificationSeconds\":0,\"maxNotifications\":1,\"notificationIntervalSeconds\":120,\"resetIntervalSeconds\":3600,\"timezone\":\"America/Los_Angeles\",\"locale\":\"en-US\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/9dd2519e-337c-45de-a66a-ff790df4dec4",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:02:13.000Z",
            "event": "EDGE_BGP_NEIGHBOR_DOWN",
            "category": "EDGE",
            "severity": "INFO",
            "message": "BGP session down for edge [branch1-vedge] to neighbor IP: [172.16.1.1]",
            "detail": "{\"remoteIp\":\"70.1.0.1\",\"method\":\"edge/edgeHeartbeat\",\"principle\":\"3b5040b0-c005-427c-8565-de8d8bf3fdc9\",\"principleType\":\"EDGE\",\"requestId\":1736265735303,\"pid\":42543,\"jobId\":\"3b5040b0-c005-42~fdc9.173624066.1830\",\"enterpriseId\":1}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/2958a549-5512-43bc-b5a5-28463c1a5c33",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:18.000Z",
            "event": "EDGE_PHYSICAL_LINK_UP",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  WAN link GE3 is up",
            "detail": "{\"physicalInterface\":\"eth5\",\"logicalInterface\":\"GE3\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/fb9f99d6-e854-4ac9-9445-22928aec0180",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:19.000Z",
            "event": "EDGE_PHYSICAL_LINK_DOWN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  LAN link GE2 is down",
            "detail": "{\"physicalInterface\":\"eth3\",\"logicalInterface\":\"GE2\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/ba3f96c3-f660-46d6-8e57-b8054ca3c251",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:19.000Z",
            "event": "LINK_ALIVE",
            "category": "NETWORK",
            "severity": "INFO",
            "message": "Link GE3 is no longer DEAD",
            "detail": "{\"logicalId\":\"88:a2:5e:e2:d1:c1:0000\",\"internalId\":\"00000003-c005-427c-8565-de8d8bf3fdc9\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/622bb4a4-0cdd-461e-a9e2-c0258c3f1023",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:13.000Z",
            "event": "LINK_DEAD",
            "category": "NETWORK",
            "severity": "ALERT",
            "message": "Link GE4 is now DEAD",
            "detail": "{\"logicalId\":\"88:a2:5e:e2:d1:c1:0000\",\"internalId\":\"00000004-d0e4-421b-9cc2-f1193cecad33\",\"edgeSerialNumber\":\"VMware-423cc4105010793f-ceeba0f112f5cf18\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/cd6e13f0-1bc0-4680-b7fd-41eacb61d898",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:07.000Z",
            "event": "EDGE_PHYSICAL_LINK_DOWN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  WAN link GE4 is down",
            "detail": "{\"physicalInterface\":\"eth0\",\"logicalInterface\":\"GE4\",\"edgeSerialNumber\":\"VMware-423cc4105010793f-ceeba0f112f5cf18\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/51ca1b92-24ce-4e3e-9d89-26081d385c41",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T15:59:23.000Z",
            "event": "LINK_DEAD",
            "category": "NETWORK",
            "severity": "ALERT",
            "message": "Link GE3 is now DEAD",
            "detail": "{\"logicalId\":\"88:a2:5e:e2:d1:c1:0000\",\"internalId\":\"00000003-c005-427c-8565-de8d8bf3fdc9\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/a8f03c1f-e847-4512-81a1-5358a54fcee8",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T15:59:17.000Z",
            "event": "EDGE_PHYSICAL_LINK_DOWN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  WAN link GE3 is down",
            "detail": "{\"physicalInterface\":\"eth5\",\"logicalInterface\":\"GE3\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/5480e3e0-688a-4c29-b44f-22b024ee4e40",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T16:01:15.000Z",
            "event": "EDGE_DOWN",
            "category": "EDGE",
            "severity": "ERROR",
            "message": "Edge [branch1-vedge] is not communicating with the Orchestrator",
            "detail": "{\"enterpriseAlertConfigurationId\":null,\"enterpriseId\":1,\"edgeId\":4,\"edgeName\":\"branch1-vedge\",\"state\":\"PENDING\",\"stateSetTime\":\"2025-01-07T16:01:15.060Z\",\"triggerTime\":\"2025-01-07T16:01:15.060Z\",\"remainingNotifications\":1,\"nextNotificationTime\":\"2025-01-07T16:01:15.060Z\",\"lastContact\":\"2025-01-07T15:58:47.548Z\",\"name\":\"EDGE_DOWN\",\"type\":\"EDGE_DOWN\",\"firstNotificationSeconds\":0,\"maxNotifications\":1,\"notificationIntervalSeconds\":120,\"resetIntervalSeconds\":3600,\"timezone\":\"America/Los_Angeles\",\"locale\":\"en-US\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/6fd7f526-121e-421b-94c9-76144a4b5092",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T15:59:45.000Z",
            "event": "BROWSER_ENTERPRISE_LOGIN",
            "category": "USER",
            "severity": "INFO",
            "message": "kmikholap@osigalaxy.com from [51.0.0.253]",
            "detail": "{\"userType\":\"ENTERPRISE\",\"remoteIp\":\"51.0.0.253\",\"username\":\"kmikholap@osigalaxy.com\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/fc3e27d1-4474-48af-88cf-22862c7689cb"
        },
        {
            "eventTime": "2025-01-07T15:18:58.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"38b0239a-f1f5-4d1b-9f4c-28b43a4258cc\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/188704ee-c97b-4d12-a3b4-cff88fe2f1a4",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/38b0239a-f1f5-4d1b-9f4c-28b43a4258cc"
            }
        },
        {
            "eventTime": "2025-01-07T15:18:54.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"01d7f9ad-d0e4-421b-9cc2-f1193cecad33\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/4e62bfe6-ee64-46b2-a140-fac310292b55",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T15:18:49.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"3b5040b0-c005-427c-8565-de8d8bf3fdc9\",\"tests\":[{\"name\":\"INTERFACE_STATUS\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/ab0e7d6b-63cc-49ef-8f7e-c3d4ad48fa7e",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T15:16:47.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"38b0239a-f1f5-4d1b-9f4c-28b43a4258cc\",\"tests\":[{\"name\":\"ARP_DUMP\",\"parameters\":[\"{\\\"count\\\":100}\"],\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/30ee4a9c-1fcd-40dc-b180-5d1e0a4a4923",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/38b0239a-f1f5-4d1b-9f4c-28b43a4258cc"
            }
        },
        {
            "eventTime": "2025-01-07T15:16:42.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"01d7f9ad-d0e4-421b-9cc2-f1193cecad33\",\"tests\":[{\"name\":\"ARP_DUMP\",\"parameters\":[\"{\\\"count\\\":100}\"],\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/2a0384b7-619f-4471-9e35-90e0a514f9a9",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T15:16:38.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"3b5040b0-c005-427c-8565-de8d8bf3fdc9\",\"tests\":[{\"name\":\"ARP_DUMP\",\"parameters\":[\"{\\\"count\\\":100}\"],\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/49cbaeb6-4119-4890-a054-fca6566bf1dd",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:43:41.000Z",
            "event": "EDGE_SSH_LOGOUT",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "sshd[3288676]: Disconnected from user root 51.0.0.253 port 1080",
            "detail": "{\"username\":\"root\",\"source\":\"51.0.0.253\",\"timestamp\":\"2025-01-07T14:43:40.745\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/f30316ef-14c4-4669-808e-83c7f64ffbc5",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:36:25.000Z",
            "event": "EDGE_SSH_LOGIN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "sshd[3288676]: Accepted keyboard-interactive/pam for root from 51.0.0.253 port 1080 ssh2",
            "detail": "{\"type\":\"keyboard-interactive/pam\",\"username\":\"root\",\"source\":\"51.0.0.253\",\"timestamp\":\"2025-01-07T14:36:25.122\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/e4742c5d-030c-428a-b5ab-02343ebb690f",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:59.000Z",
            "event": "EDGE_PHYSICAL_LINK_UP",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  WAN link GE3 is up",
            "detail": "{\"physicalInterface\":\"eth5\",\"logicalInterface\":\"GE3\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/de659e98-dca3-4a84-bb31-30202bc51c9e",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:47.000Z",
            "event": "EDGE_PHYSICAL_LINK_DOWN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  WAN link GE3 is down",
            "detail": "{\"physicalInterface\":\"eth5\",\"logicalInterface\":\"GE3\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/15af8f45-e200-4b03-b8db-4930ae83a619",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:48.000Z",
            "event": "EDGE_PHYSICAL_LINK_DOWN",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  LAN link GE2 is down",
            "detail": "{\"physicalInterface\":\"eth3\",\"logicalInterface\":\"GE2\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/f75a7fc1-67b2-4123-9d58-741676bb999d",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:55.000Z",
            "event": "EDGE_AUTO_SIM_SWITCH",
            "category": "EDGE",
            "severity": "NOTICE",
            "message": "Autosim Switch Disabled",
            "detail": "Auto SIM switchover disabled edgeSerialNumber: VMware-423cb2ae8d287d64-ae7ee956813f0145",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/1a683521-2a2b-4c2a-8349-a06716424902",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:59.000Z",
            "event": "EDGE_PHYSICAL_LINK_UP",
            "category": "SYSTEM",
            "severity": "INFO",
            "message": "Edge  LAN link GE2 is up",
            "detail": "{\"physicalInterface\":\"eth3\",\"logicalInterface\":\"GE2\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/2cfbd266-4d23-4ea8-ab02-cd60423d40fe",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:31:00.000Z",
            "event": "LINK_ALIVE",
            "category": "NETWORK",
            "severity": "INFO",
            "message": "Link GE3 is no longer DEAD",
            "detail": "{\"logicalId\":\"88:a2:5e:e2:d1:c1:0000\",\"internalId\":\"00000003-c005-427c-8565-de8d8bf3fdc9\",\"edgeSerialNumber\":\"VMware-423cb2ae8d287d64-ae7ee956813f0145\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/fa485f54-a95d-44cc-b63c-cd5d59dd4d69",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:30:17.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "restartService",
            "detail": "[{\"action\":\"restartService\",\"parameters\":{}}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/c5dac6c0-2b10-479b-ba91-4f7632468cff",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:19:08.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "enterLiveLinkStatsMode",
            "detail": "[{\"action\":\"enterLiveLinkStatsMode\",\"parameters\":{}}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/612ae8e8-9cf9-40eb-98dc-6242a42822b3",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        },
        {
            "eventTime": "2025-01-07T14:16:52.000Z",
            "event": "BROWSER_ENTERPRISE_LOGIN",
            "category": "USER",
            "severity": "INFO",
            "message": "kmikholap@osigalaxy.com from [51.0.0.253]",
            "detail": "{\"userType\":\"ENTERPRISE\",\"remoteIp\":\"51.0.0.253\",\"username\":\"kmikholap@osigalaxy.com\"}",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/cab4e6c6-c782-43ec-a7fa-bb0337e34b74"
        },
        {
            "eventTime": "2025-01-07T13:16:34.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"38b0239a-f1f5-4d1b-9f4c-28b43a4258cc\",\"tests\":[{\"name\":\"RESTART_DNSMASQ\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/a0869a39-309b-43d9-8207-fd206acc99a8",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/38b0239a-f1f5-4d1b-9f4c-28b43a4258cc"
            }
        },
        {
            "eventTime": "2025-01-07T13:16:31.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"01d7f9ad-d0e4-421b-9cc2-f1193cecad33\",\"tests\":[{\"name\":\"RESTART_DNSMASQ\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/11434b50-bf1e-4c9f-b9d7-55215e5e2775",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/01d7f9ad-d0e4-421b-9cc2-f1193cecad33"
            }
        },
        {
            "eventTime": "2025-01-07T13:16:28.000Z",
            "event": "REMOTE_ACTION",
            "category": "EDGE",
            "severity": "INFO",
            "message": "runDiagnostics",
            "detail": "[{\"logicalId\":\"3b5040b0-c005-427c-8565-de8d8bf3fdc9\",\"tests\":[{\"name\":\"RESTART_DNSMASQ\",\"resformat\":\"JSON\"}]}]",
            "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events/24b50375-0d3a-4fa2-95c8-c0adb80f6c9e",
            "edge": {
                "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/edges/3b5040b0-c005-427c-8565-de8d8bf3fdc9"
            }
        }
    ],
    "_href": "/api/sdwan/v2/enterprises/b3512d36-ab2b-4bce-b61a-aeff7d93ab37/events?start=1736252188168&end=1736266588168"
}
