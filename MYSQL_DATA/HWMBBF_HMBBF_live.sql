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
-- Table structure for table `HMBBF_live`
--

DROP TABLE IF EXISTS `HMBBF_live`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HMBBF_live` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `live_name` varchar(256) NOT NULL,
  `time_begin` time(6) NOT NULL,
  `time_end` time(6) NOT NULL,
  `vedio_url` longtext NOT NULL,
  `date` date NOT NULL,
  `time` longtext NOT NULL,
  `status` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `is_collect` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HMBBF_live`
--

LOCK TABLES `HMBBF_live` WRITE;
/*!40000 ALTER TABLE `HMBBF_live` DISABLE KEYS */;
INSERT INTO `HMBBF_live` VALUES (1,'跨产业合作使能全联接世界','09:00:00.000000','12:30:00.000000','https://engage.vevent.com/rt/huawei/log_thru.jsp?seid=2443&standaloneparam=txnMJJDz-akcSzOvg93i2u6VXKnKwq14Mv7ZtIeszVnCDUcFDMI3rksg2I-SeDEj6qwl78JthaMvn61hhRvQq1kgIfQ6MViSneMYPo4Dd10','2016-11-24','',2,1,0),(2,'数字化联合创新实现商业成功(视频、机器人/人工智能) ','14:00:00.000000','18:10:00.000000','https://engage.vevent.com/rt/huawei/log_thru.jsp?seid=2455&standaloneparam=txnMJJDz-akcSzOvg93i2u6VXKnKwq14Mv7ZtIeszVnCDUcFDMI3rksg2I-SeDEjuvXBWkGWqBO1flBecHcgEw6hBsUz-n9KpNeenxPSiC8','2016-11-24','',2,1,0),(3,'产业生态与网络创新','09:00:00.000000','13:10:00.000000','https://engage.vevent.com/rt/huawei/log_thru.jsp?seid=2467&standaloneparam=txnMJJDz-akcSzOvg93i2u6VXKnKwq14Mv7ZtIeszVnCDUcFDMI3rksg2I-SeDEjPuRfgrgjC6Eej8CiSV0Yl54cqGLwpGlmTYnTaexJ2CA','2016-11-25','',2,1,0);
/*!40000 ALTER TABLE `HMBBF_live` ENABLE KEYS */;
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
