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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-12-02 02:41:52.628385'),(2,'auth','0001_initial','2016-12-02 02:41:52.910721'),(3,'admin','0001_initial','2016-12-02 02:41:52.984215'),(4,'contenttypes','0002_remove_content_type_name','2016-12-02 02:41:53.106078'),(5,'auth','0002_alter_permission_name_max_length','2016-12-02 02:41:53.142150'),(6,'auth','0003_alter_user_email_max_length','2016-12-02 02:41:53.179007'),(7,'auth','0004_alter_user_username_opts','2016-12-02 02:41:53.199712'),(8,'auth','0005_alter_user_last_login_null','2016-12-02 02:41:53.262616'),(9,'auth','0006_require_contenttypes_0002','2016-12-02 02:41:53.265537'),(10,'sessions','0001_initial','2016-12-02 02:41:53.308888'),(11,'HMBBF','0001_initial','2016-12-02 02:56:23.991644'),(12,'HMBBF','0002_home_news','2016-12-02 06:46:06.110509'),(13,'HMBBF','0003_auto_20161202_0649','2016-12-02 06:49:21.344022'),(14,'HMBBF','0004_home_seacher_keyword','2016-12-02 07:06:57.550917'),(15,'HMBBF','0005_auto_20161202_0721','2016-12-02 07:21:17.417204'),(16,'HMBBF','0006_guest','2016-12-02 08:35:02.920214'),(17,'HMBBF','0007_auto_20161202_0840','2016-12-02 08:41:03.302821'),(18,'HMBBF','0008_auto_20161202_0854','2016-12-02 09:00:41.499114'),(19,'HMBBF','0009_auto_20161202_0900','2016-12-02 09:00:41.501922'),(20,'HMBBF','0010_guest_home_ad_home_keyword_home_news','2016-12-02 09:01:50.111230'),(21,'HMBBF','0011_auto_20161202_0901','2016-12-02 09:01:50.115564'),(22,'HMBBF','0012_guest','2016-12-02 09:13:35.513482'),(23,'HMBBF','0013_home_ad_home_keyword_home_news','2016-12-02 09:13:35.517188'),(24,'HMBBF','0014_theme','2016-12-02 09:27:52.704428'),(25,'HMBBF','0015_auto_20161202_1733','2016-12-02 09:33:44.720916'),(26,'HMBBF','0016_remove_theme_time','2016-12-02 09:41:45.188225'),(27,'HMBBF','0017_theme_time','2016-12-02 09:43:45.845525'),(28,'HMBBF','0018_auto_20161205_0929','2016-12-05 01:29:49.548649'),(29,'HMBBF','0019_auto_20161205_0934','2016-12-05 01:34:14.305560'),(30,'HMBBF','0020_auto_20161205_0934','2016-12-05 01:34:31.074670'),(31,'HMBBF','0021_auto_20161205_0937','2016-12-05 01:37:42.877213'),(32,'HMBBF','0022_auto_20161205_0938','2016-12-05 01:38:09.471761'),(33,'HMBBF','0023_auto_20161205_0946','2016-12-05 01:46:02.721857'),(34,'HMBBF','0024_auto_20161205_1007','2016-12-05 02:07:47.448140'),(35,'HMBBF','0025_remove_theme_time','2016-12-05 02:22:54.976819'),(36,'HMBBF','0026_auto_20161205_1026','2016-12-05 02:26:11.040043'),(37,'HMBBF','0027_auto_20161205_1032','2016-12-05 02:32:09.608534'),(38,'HMBBF','0028_auto_20161205_1032','2016-12-05 02:32:28.298243'),(39,'HMBBF','0029_auto_20161205_1040','2016-12-05 02:40:50.746211'),(40,'HMBBF','0030_auto_20161205_1041','2016-12-05 02:41:42.870340'),(41,'HMBBF','0031_auto_20161205_1042','2016-12-05 02:42:33.041596'),(42,'HMBBF','0032_auto_20161205_1042','2016-12-05 02:42:58.357963'),(43,'HMBBF','0033_auto_20161205_1043','2016-12-05 02:43:27.430879'),(44,'HMBBF','0034_auto_20161205_1045','2016-12-05 02:45:48.770810'),(45,'HMBBF','0035_theme_theme_name','2016-12-05 06:59:51.647180'),(46,'HMBBF','0036_live','2016-12-06 02:12:16.117842'),(47,'HMBBF','0037_auto_20161206_1014','2016-12-06 02:14:59.217011'),(48,'HMBBF','0038_auto_20161206_1017','2016-12-06 02:17:21.000094');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-06 11:42:01