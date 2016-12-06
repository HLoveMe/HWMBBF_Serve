-- MySQL dump 10.13  Distrib 5.7.9, for osx10.9 (x86_64)
--
-- Host: localhost    Database: HWMBBF
-- ------------------------------------------------------
-- Server version	5.7.13

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
-- Table structure for table `HMBBF_theme_theme_guest`
--

DROP TABLE IF EXISTS `HMBBF_theme_theme_guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HMBBF_theme_theme_guest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `theme_id` int(11) NOT NULL,
  `guest_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `theme_id` (`theme_id`,`guest_id`),
  KEY `HMBBF_theme_theme_gu_guest_id_36513ddc28b8b308_fk_HMBBF_guest_id` (`guest_id`),
  CONSTRAINT `HMBBF_theme_theme_gu_guest_id_36513ddc28b8b308_fk_HMBBF_guest_id` FOREIGN KEY (`guest_id`) REFERENCES `HMBBF_guest` (`id`),
  CONSTRAINT `HMBBF_theme_theme_gu_theme_id_300e749f4113c4cd_fk_HMBBF_theme_id` FOREIGN KEY (`theme_id`) REFERENCES `HMBBF_theme` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=390 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HMBBF_theme_theme_guest`
--

LOCK TABLES `HMBBF_theme_theme_guest` WRITE;
/*!40000 ALTER TABLE `HMBBF_theme_theme_guest` DISABLE KEYS */;
INSERT INTO `HMBBF_theme_theme_guest` VALUES (294,1,1),(295,2,27),(296,3,28),(298,4,33),(297,5,106),(299,7,34),(300,8,31),(301,10,35),(302,12,22),(303,13,36),(304,14,131),(305,15,37),(306,17,29),(307,18,38),(308,19,39),(309,20,40),(315,21,53),(311,21,65),(310,21,102),(313,21,103),(314,21,104),(312,21,138),(316,23,135),(317,25,43),(318,26,44),(319,27,45),(327,30,46),(328,32,54),(339,36,64),(373,38,140),(355,39,137),(383,40,101),(329,41,55),(331,42,56),(332,43,57),(334,44,58),(335,50,142),(337,51,61),(340,52,65),(356,53,88),(357,54,96),(358,55,139),(365,56,135),(367,57,85),(366,58,84),(368,59,83),(369,60,81),(370,62,80),(371,63,82),(372,64,137),(374,65,77),(375,66,76),(376,67,75),(378,68,74),(377,70,71),(381,72,70),(382,73,97),(384,74,69),(385,75,68),(386,76,78),(387,77,66),(388,78,141),(389,79,99),(336,80,103),(341,81,64),(342,81,110),(343,81,111),(344,81,136),(330,82,114),(333,83,114),(338,84,114),(345,85,115),(346,85,116),(347,85,118),(348,85,119),(349,85,120),(350,86,64),(351,86,121),(352,86,122),(353,86,123),(354,86,124),(359,87,125),(360,87,126),(362,87,128),(363,87,129),(364,87,130),(361,87,139),(380,90,133),(379,91,73),(320,92,108),(321,93,107),(324,93,109),(322,93,132),(325,93,133),(326,93,134),(323,93,135);
/*!40000 ALTER TABLE `HMBBF_theme_theme_guest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-06 11:42:02
