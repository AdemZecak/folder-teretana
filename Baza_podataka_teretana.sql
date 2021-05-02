-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: teretana
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clanstvo`
--

DROP TABLE IF EXISTS `clanstvo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clanstvo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ime_clanstva` varchar(40) DEFAULT NULL,
  `cijena_clanstva` int DEFAULT NULL,
  `trajanje_clanstva` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clanstvo`
--

LOCK TABLES `clanstvo` WRITE;
/*!40000 ALTER TABLE `clanstvo` DISABLE KEYS */;
INSERT INTO `clanstvo` VALUES (1,'jednomjesecno',50,31),(2,'tromjesecno',130,90),(3,'polugodisnje',265,182),(4,'godisnje',500,365);
/*!40000 ALTER TABLE `clanstvo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `klijenti`
--

DROP TABLE IF EXISTS `klijenti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `klijenti` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ime_klijenta` varchar(40) DEFAULT NULL,
  `prezime_klijenta` varchar(40) DEFAULT NULL,
  `username` varchar(40) DEFAULT NULL,
  `passwd` varchar(60) DEFAULT NULL,
  `jmbg_klijenta` varchar(250) DEFAULT NULL,
  `id_kartice` varchar(250) DEFAULT NULL,
  `ime_clanstva` varchar(60) DEFAULT NULL,
  `clanstvo_pocelo` varchar(200) DEFAULT NULL,
  `clanstvo_zavrsava` varchar(200) DEFAULT NULL,
  `trajanje_clanstva` varchar(200) DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `rfm` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `klijenti`
--

LOCK TABLES `klijenti` WRITE;
/*!40000 ALTER TABLE `klijenti` DISABLE KEYS */;
INSERT INTO `klijenti` VALUES (1,'Adem','Zecak','adem','zecak','783427852783','321812671','polugodisnje','2021-04-08','2021-10-07 21:25:20.980348','182 dana',23.9591,24.4278),(2,'Jenny','m','jenny','m','784738784343','1673125599','tromjesecno','2021-04-08','2021-07-07 21:34:21.608652','90 dana',22.4914,31.4391),(3,'Bruce','Banner','Hulk','hulk123','78438748743','363761269','polugodisnje','2021-04-08','2021-10-07 21:35:34.107266','182 dana',22.7267,23.5117),(4,'Marko','Markanovic','marko','marko123','74238745','949330455','godisnje','2021-04-08','2022-04-08 21:51:57.762374','365 dana',26.8787,25.6327),(5,'Mike','M','mike','m','28148921858921','995585736','tromjesecno','2021-04-09','2021-07-08 11:52:22.539795','90 dana',27.7769,27.8384),(6,'Didier','Drogba','drogba','drogba123','8952375823758923','308765753','tromjesecno','2021-04-09','2021-07-08 12:13:47.005103','90 dana',22.8797,21.6087),(7,'Timn','M','tim','123','875285823','547111260','tromjesecno','2021-04-09','2021-07-08 12:14:54.651142','90 dana',23.7654,21.6471),(8,'Adrian','Smith','adrian','smith','389523759823','6030291339','polugodisnje','2021-04-09','2021-10-08 12:16:39.260249','182 dana',20.7612,18.6667),(9,'fas','jfldsh','jfkadsh','sfa','8735278','7648719511','tromjesecno','2021-04-09','2021-07-08 12:20:22.297236','90 dana',19.0311,11.6923),(10,'Brian','Griffin','brian','griffin','38952858293895','193762210','godisnje','2021-04-09','2022-04-09 14:33:50.952403','365 dana',25.7117,21.6923),(11,'pink','floyd','pink','floyd','38925753287953274','456127547','tromjesecno','2021-04-09','2021-07-08 14:34:54.515039','90 dana',24.9307,35.7884),(12,'Alex','Monkeys','alex ','turner','481398549138','247690719','godisnje','2021-04-21','2022-04-21 21:56:51.155122','365 dana',22.9071,22.7368),(13,'Anne','M','anne','m','85328958923','48734676','polugodisnje','2021-05-01','2021-10-30 23:14:07.959805','182 dana',18.8268,30.8052),(14,'jhdsaj','jhfas','jdsa','jfhads','841238945231','914971375','polugodisnje','2021-05-01','2021-10-30 23:15:38.979011','182 dana',24.5779,22.8372),(15,'hkjasd','jkfash','hjsfa','hjadsf','839148','4123837572','polugodisnje','2021-05-01','2021-10-30 23:18:33.580998','182 dana',24.8981,21.2727),(16,'Bruce','Dickinson','bruce1','bruce','835428358','941186276','tromjesecno','2021-05-01','2021-07-30 23:20:20.988141','90 dana',21.9138,19.9524),(17,'aaa','bbb','aaa','bbb','78418732481','2253318056','polugodisnje','2021-05-01','2021-10-30 23:26:45.060109','182 dana',24.8981,23.1304),(18,'bb','nn','bb','nn','841832845132','1772865320','polugodisnje','2021-05-01','2021-10-30 23:50:01.857001','182 dana',24.5779,35.7727),(20,'jafs','hjadsf','hjfsa','hjsaf','895328952','108379314','tromjesecno','2021-05-02','2021-07-31 15:13:34.441178','90 dana',21.0667,23.1642);
/*!40000 ALTER TABLE `klijenti` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-02 16:39:07
