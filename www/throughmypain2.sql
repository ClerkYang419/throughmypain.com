CREATE DATABASE  IF NOT EXISTS `throughmypain` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `throughmypain`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: throughmypain
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `Cells`
--

DROP TABLE IF EXISTS `Cells`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cells` (
  `Cell_ID` varchar(50) NOT NULL,
  `cell_severity` int(11) NOT NULL,
  `Region_ID` varchar(50) NOT NULL,
  PRIMARY KEY (`Cell_ID`),
  KEY `Region_ID_idx` (`Region_ID`),
  CONSTRAINT `Region_ID` FOREIGN KEY (`Region_ID`) REFERENCES `Regions` (`Region_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Pains`
--

DROP TABLE IF EXISTS `Pains`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pains` (
  `Pain_ID` varchar(50) NOT NULL,
  `region_count` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  `pain_character` varchar(50) NOT NULL,
  `pain_severity` int(11) NOT NULL,
  `depth` varchar(50) NOT NULL,
  `frequency` varchar(50) NOT NULL,
  `Users_User_ID` varchar(50) NOT NULL,
  `create_at` varchar(50) NOT NULL,
  `regions` varchar(4000) NOT NULL,
  PRIMARY KEY (`Pain_ID`),
  KEY `fk_Pains_Users1_idx` (`Users_User_ID`),
  CONSTRAINT `fk_Pains_Users1` FOREIGN KEY (`Users_User_ID`) REFERENCES `Users` (`User_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Record_cache`
--

DROP TABLE IF EXISTS `Record_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Record_cache` (
  `Record_ID` varchar(50) NOT NULL,
  `record_brief` varchar(100) NOT NULL,
  `pain_list` varchar(20000) NOT NULL,
  PRIMARY KEY (`Record_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Regions`
--

DROP TABLE IF EXISTS `Regions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Regions` (
  `Region_ID` varchar(50) NOT NULL,
  `region_severity` int(11) NOT NULL,
  `cells_count` int(11) NOT NULL,
  `Pain_ID` varchar(50) NOT NULL,
  PRIMARY KEY (`Region_ID`),
  KEY `Pain_ID_idx` (`Pain_ID`),
  CONSTRAINT `Pain_ID` FOREIGN KEY (`Pain_ID`) REFERENCES `Pains` (`Pain_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Reports`
--

DROP TABLE IF EXISTS `Reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Reports` (
  `Report_ID` varchar(50) NOT NULL,
  `chart_number` int(11) NOT NULL,
  `create_at` varchar(50) NOT NULL,
  `User_ID` varchar(50) NOT NULL,
  PRIMARY KEY (`Report_ID`),
  KEY `User_ID_idx` (`User_ID`),
  CONSTRAINT `user` FOREIGN KEY (`User_ID`) REFERENCES `Users` (`User_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `User_ID` varchar(50) NOT NULL,
  `user_passwd` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `pains_number` int(11) NOT NULL,
  `last_record_date` varchar(50) NOT NULL,
  `create_at` varchar(50) NOT NULL,
  `admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`User_ID`),
  UNIQUE KEY `index_user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `records`
--

DROP TABLE IF EXISTS `records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `records` (
  `Record_ID` varchar(50) NOT NULL,
  `create_at` varchar(50) NOT NULL,
  `pain_number` int(11) NOT NULL,
  `record_brief` varchar(100) NOT NULL,
  `User_ID` varchar(50) NOT NULL,
  `pains_list` varchar(20000) NOT NULL,
  PRIMARY KEY (`Record_ID`),
  KEY `User_ID_idx` (`User_ID`),
  CONSTRAINT `User_ID` FOREIGN KEY (`User_ID`) REFERENCES `Users` (`User_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-20 12:58:03
