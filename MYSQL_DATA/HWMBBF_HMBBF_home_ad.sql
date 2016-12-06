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
-- Table structure for table `HMBBF_home_ad`
--

DROP TABLE IF EXISTS `HMBBF_home_ad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `HMBBF_home_ad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ad_name` varchar(1024) NOT NULL,
  `ad_name_en` varchar(1024) NOT NULL,
  `type` varchar(1024) NOT NULL,
  `target_id` varchar(1024) NOT NULL,
  `banner_img` varchar(1024) NOT NULL,
  `banner_img_en` varchar(1024) NOT NULL,
  `ad_url` varchar(1024) NOT NULL,
  `ad_url_en` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `HMBBF_home_ad`
--

LOCK TABLES `HMBBF_home_ad` WRITE;
/*!40000 ALTER TABLE `HMBBF_home_ad` DISABLE KEYS */;
INSERT INTO `HMBBF_home_ad` VALUES (6,'丁耘：5G建设从现在起步 ','Huawei Launches First Systematic Methodology for IoT Network Planning','0','18','http://huawei.vr68.com/Public/images/upload/5836e0d1c68e3.jpg','http://huawei.vr68.com/Public/images/upload/5837be212473d.jpg','http://www.huawei.com/cn/news/2016/11/Dingyun-On-the-Road-to-5G','http://www.huawei.com/en/news/2016/11/Dingyun-On-the-Road-to-5G'),(10,'华为阐述无线网络全云化理念','Huawei Unveils Vision for All Cloud Mobile Networks','0','1','http://huawei.vr68.com/Public/images/upload/583929b626bbc.jpg','http://huawei.vr68.com/Public/images/upload/583929be14b2b.jpg','http://www.huawei.com/minisite/hwmbbf16/cn/insight.html','http://www.huawei.com/minisite/hwmbbf16/en/insight.html'),(11,'华为轮值CEO胡厚崑发布移动宽带X Labs计划 ','Three Labs for Building Application-Centric Networks in Three Major Markets','0','5','http://huawei.vr68.com/Public/images/upload/5836dfad320e3.jpg','http://huawei.vr68.com/Public/images/upload/5837bd8d47837.jpg','http://www.huawei.com/cn/news/2016/11/kenHu-MBBF-XLabs','http://www.huawei.com/en/news/2016/11/kenHu-MBBF-XLabs');
/*!40000 ALTER TABLE `HMBBF_home_ad` ENABLE KEYS */;
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
