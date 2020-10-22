-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: employee
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `emp_family`
--

DROP TABLE IF EXISTS `emp_family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_family` (
  `ID` int DEFAULT NULL,
  `emp_id` int DEFAULT NULL,
  `Relation` varchar(50) NOT NULL,
  `Gender` varchar(50) NOT NULL,
  KEY `fk_id` (`emp_id`),
  CONSTRAINT `fk_id` FOREIGN KEY (`emp_id`) REFERENCES `rest_emp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_family`
--

LOCK TABLES `emp_family` WRITE;
/*!40000 ALTER TABLE `emp_family` DISABLE KEYS */;
INSERT INTO `emp_family` VALUES (1,1,'Father','M'),(2,2,'Sister','F'),(3,1,'Brother','M'),(4,2,'Mother','F');
/*!40000 ALTER TABLE `emp_family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emp_project`
--

DROP TABLE IF EXISTS `emp_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_project` (
  `project_id` int DEFAULT NULL,
  `emp_id` int DEFAULT NULL,
  `project_name` varchar(50) NOT NULL,
  `domain_name` varchar(50) NOT NULL,
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `emp_id` FOREIGN KEY (`emp_id`) REFERENCES `rest_emp` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_project`
--

LOCK TABLES `emp_project` WRITE;
/*!40000 ALTER TABLE `emp_project` DISABLE KEYS */;
INSERT INTO `emp_project` VALUES (3,4,'Annotation','ML'),(3,4,'Annotation','ML'),(2,1,'AUDI','POWERTRAIN'),(3,2,'BMW','Image Processing'),(4,2,'TATA','AI');
/*!40000 ALTER TABLE `emp_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rest_emp`
--

DROP TABLE IF EXISTS `rest_emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rest_emp` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `age` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rest_emp`
--

LOCK TABLES `rest_emp` WRITE;
/*!40000 ALTER TABLE `rest_emp` DISABLE KEYS */;
INSERT INTO `rest_emp` VALUES (1,'Urmila',26),(2,'Nikita',20),(3,'Ajinkya',22),(4,'Ashwin',21),(5,'Nikhil',29);
/*!40000 ALTER TABLE `rest_emp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-22 11:28:20
