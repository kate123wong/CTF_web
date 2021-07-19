-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: socialcontact
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Infos`
--

DROP TABLE IF EXISTS `Infos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Infos` (
  `conid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `content` text,
  `num` int(11) DEFAULT NULL,
  PRIMARY KEY (`conid`),
  KEY `uid_idx` (`uid`),
  CONSTRAINT `uid` FOREIGN KEY (`uid`) REFERENCES `Users` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Infos`
--

LOCK TABLES `Infos` WRITE;
/*!40000 ALTER TABLE `Infos` DISABLE KEYS */;
/*!40000 ALTER TABLE `Infos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Users`
--

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
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES (148,'骏奇小公主','92a0a2d55d3e38a1de90afffb9d0f848',NULL,NULL),(149,'婉琳mio','4677c0f38c1965cbe08bb46d634bdc04',NULL,NULL),(150,'仙灵桂兰','79c3826917efc4e7dcee28d288986d13',NULL,NULL),(151,'依风小仙女','e0f99b2e29cfce1fabeb7732e24847a4',NULL,NULL),(152,'无冬代丝','59ce82bfa0a22be8bb184255ccb48c9e',NULL,NULL),(153,'和泰baby','942bc87c671b46809965218a1af8bb35',NULL,NULL),(154,'羽豆寿美恵','f779bf0451f98f6c8b4f89a5f3ee80b6',NULL,NULL),(155,'羽切冷子','0418ef425350b8046c9b3e500efb4532',NULL,NULL),(156,'tt','accc9105df5383111407fd5b41255e23','fef7f0455a7c21cf13b62ffd060086c7',NULL),(157,'艾久','22de8fe317b2ce41324a80c3ceb34904',NULL,NULL),(158,'Bruce Conan','0a592194880f10272b8e7d4ea54d8dd6',NULL,NULL),(159,'Will Pearson','2e38d34a2053dcb1ab4517859704ad65',NULL,NULL),(171,'admin','1164f9e5b8cef768396dcd5374e4b6eb','0098b35216c7a270a03688c09ba1244b','key:YkZ0VFBSbHBTMVZUODFia1R0eEU=');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-19  7:29:55
