use socialcontact;
DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `3passwd2` text CHARACTER SET latin1,
  `session` text CHARACTER SET latin1,
  `remark` text CHARACTER SET latin1,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=172 DEFAULT CHARSET=utf8;

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (148,'Annie','92a0a2d55d3e38a1de90afffb9d0f848',NULL,NULL),(149,'mio','4677c0f38c1965cbe08bb46d634bdc04',NULL,NULL),(150,'Augustine','79c3826917efc4e7dcee28d288986d13',NULL,NULL),(151,'Karam','e0f99b2e29cfce1fabeb7732e24847a4',NULL,NULL),(152,'Roscoe','59ce82bfa0a22be8bb184255ccb48c9e',NULL,NULL),(153,'baby','942bc87c671b46809965218a1af8bb35',NULL,NULL),(154,'Bear','f779bf0451f98f6c8b4f89a5f3ee80b6',NULL,NULL),(155,'Burke','0418ef425350b8046c9b3e500efb4532',NULL,NULL),(156,'Timmy','accc9105df5383111407fd5b41255e23','fef7f0455a7c21cf13b62ffd060086c7',NULL),(157,'Xenia','22de8fe317b2ce41324a80c3ceb34904',NULL,NULL),(158,'Bruce Conan','0a592194880f10272b8e7d4ea54d8dd6',NULL,NULL),(159,'Will Pearson','2e38d34a2053dcb1ab4517859704ad65',NULL,NULL),(171,'admin','1164f9e5b8cef768396dcd5374e4b6eb','0098b35216c7a270a03688c09ba1244b','key:YkZ0VFBSbHBTMVZUODFia1R0eEU=');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

