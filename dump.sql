-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: hotel
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


--
-- Table structure for table `BOOKING`
--

DROP TABLE IF EXISTS `BOOKING`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `BOOKING` (
  `bookingID` int NOT NULL AUTO_INCREMENT,
  `dobooking` date NOT NULL,
  `checkout` date NOT NULL,
  `num_rooms` int NOT NULL,
  `booking_Status` varchar(10) DEFAULT NULL,
  `num_adults` int NOT NULL,
  `num_children` int DEFAULT NULL,
  `customerID` int NOT NULL,
  `checkin` date NOT NULL,
  PRIMARY KEY (`bookingID`),
  KEY `customerID` (`customerID`),
  CONSTRAINT `BOOKING_ibfk_1` FOREIGN KEY (`customerID`) REFERENCES `CUSTOMER` (`customerID`),
  CONSTRAINT `BOOKING_chk_1` CHECK ((`num_rooms` > 0)),
  CONSTRAINT `BOOKING_chk_2` CHECK ((`num_adults` > 0)),
  CONSTRAINT `chkdate` CHECK ((`checkout` > `checkin`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BOOKING`
--

LOCK TABLES `BOOKING` WRITE;
/*!40000 ALTER TABLE `BOOKING` DISABLE KEYS */;
/*!40000 ALTER TABLE `BOOKING` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CAB`
--

DROP TABLE IF EXISTS `CAB`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CAB` (
  `cabNo` varchar(10) NOT NULL,
  `driverName` varchar(20) NOT NULL,
  `pickup` varchar(50) DEFAULT NULL,
  `pickup_landmark` varchar(10) DEFAULT NULL,
  `drop_location` varchar(50) DEFAULT NULL,
  `drop_landmark` varchar(10) DEFAULT NULL,
  `km` int DEFAULT NULL,
  `arrivalTime` time DEFAULT NULL,
  `serviceID` int NOT NULL,
  PRIMARY KEY (`cabNo`),
  KEY `serviceID` (`serviceID`),
  CONSTRAINT `CAB_ibfk_1` FOREIGN KEY (`serviceID`) REFERENCES `SERVICE` (`serviceID`),
  CONSTRAINT `CAB_chk_1` CHECK ((`km` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CAB`
--

LOCK TABLES `CAB` WRITE;
/*!40000 ALTER TABLE `CAB` DISABLE KEYS */;
/*!40000 ALTER TABLE `CAB` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `CUSTOMER` (
  `customerID` int NOT NULL AUTO_INCREMENT,
  `aadharID` varchar(16) NOT NULL,
  `customerName` varchar(50) NOT NULL,
  `email` varchar(20) DEFAULT NULL,
  `address` varchar(30) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(1) NOT NULL,
  `phoneNo` varchar(10) NOT NULL,
  PRIMARY KEY (`customerID`),
  UNIQUE KEY `aadharID` (`aadharID`),
  CONSTRAINT `check_aadhar` CHECK (regexp_like(`aadharID`,_utf8mb4'^[0-9]{16}$')),
  CONSTRAINT `check_gender_cust` CHECK ((`gender` in (_utf8mb4'M',_utf8mb4'F',_utf8mb4'O'))),
  CONSTRAINT `check_num_cust` CHECK (regexp_like(`phoneNo`,_utf8mb4'^[0-9]{10}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `DEPARTMENT`
--

DROP TABLE IF EXISTS `DEPARTMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEPARTMENT` (
  `departmentCode` int NOT NULL,
  `managerID` int,
  `departmentName` varchar(15) NOT NULL,
  PRIMARY KEY (`departmentCode`),
  UNIQUE KEY `departmentName` (`departmentName`),
  KEY `managerID` (`managerID`),
  CONSTRAINT `DEPARTMENT_ibfk_1` FOREIGN KEY (`managerID`) REFERENCES `EMPLOYEE` (`employeeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPARTMENT`
--

LOCK TABLES `DEPARTMENT` WRITE;
/*!40000 ALTER TABLE `DEPARTMENT` DISABLE KEYS */;
INSERT INTO `DEPARTMENT` VALUES (1,NULL,'Reception'), (2,1,'Travel Desk'), (3,2,'Restaurant'), (4,NULL,'Housekeeping'),(5,NULL,'Security');
/*!40000 ALTER TABLE `DEPARTMENT` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `EMPLOYEE`
--

DROP TABLE IF EXISTS `EMPLOYEE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EMPLOYEE` (
  `employeeID` int NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `address` varchar(30) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(1) NOT NULL,
  `phoneNo` varchar(10) NOT NULL,
  `salary` int NOT NULL,
  `deptcode` int NOT NULL,
  `superID` int DEFAULT NULL,
  PRIMARY KEY (`employeeID`),
  KEY `deptcode` (`deptcode`),
  KEY `superID` (`superID`),
  CONSTRAINT `EMPLOYEE_ibfk_1` FOREIGN KEY (`deptcode`) REFERENCES `DEPARTMENT` (`departmentCode`),
  CONSTRAINT `EMPLOYEE_ibfk_2` FOREIGN KEY (`superID`) REFERENCES `EMPLOYEE` (`employeeID`),
  CONSTRAINT `check_gender` CHECK ((`gender` in (_utf8mb4'M',_utf8mb4'F',_utf8mb4'O'))),
  CONSTRAINT `check_num` CHECK (regexp_like(`phoneNo`,_utf8mb4'^[0-9]{10}$')),
  CONSTRAINT `check_salary` CHECK ((`salary` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EMPLOYEE`
--

LOCK TABLES `EMPLOYEE` WRITE;
/*!40000 ALTER TABLE `EMPLOYEE` DISABLE KEYS */;
INSERT INTO `EMPLOYEE` VALUES (1,'abc@gmail.com','home sweet home','hyderabad','telangana','india','2001-12-01','F','1234567890',3213,2,NULL),(2,'abc@gmail.com','iiit','mumbai','maharashtra','india','2001-09-01','M','9934567890',4213,3,NULL),(3,'abdedc@gmail.com','blahblahblha','patna','bihar','india','1998-03-01','F','8834567890',65463,2,1);
/*!40000 ALTER TABLE `EMPLOYEE` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `DEPENDENT`
--

DROP TABLE IF EXISTS `DEPENDENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `DEPENDENT` (
  `name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `phoneNo` varchar(10) NOT NULL,
  `employeeID` int NOT NULL,
  PRIMARY KEY (`name`),
  KEY `employeeID` (`employeeID`),
  CONSTRAINT `DEPENDENT_ibfk_1` FOREIGN KEY (`employeeID`) REFERENCES `EMPLOYEE` (`employeeID`),
  CONSTRAINT `check_num_dep` CHECK (regexp_like(`phoneNo`,_utf8mb4'^[0-9]{10}$'))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `DEPENDENT`
--

LOCK TABLES `DEPENDENT` WRITE;
/*!40000 ALTER TABLE `DEPENDENT` DISABLE KEYS */;
INSERT INTO `DEPENDENT` VALUES ('Harshit', '2001-03-23','9876543210',1), ('Eshika','2001-12-04','5643173826',2),('Adith John Rajeev', '1998-02-01','9871324536',3);
/*!40000 ALTER TABLE `DEPENDENT` ENABLE KEYS */;
UNLOCK TABLES;




--
-- Table structure for table `NUMOFNIGHTS`
--

DROP TABLE IF EXISTS `NUMOFNIGHTS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NUMOFNIGHTS` (
  `checkin` date NOT NULL,
  `checkout` date NOT NULL,
  `numofnights` int DEFAULT NULL,
  `bookingID` int PRIMARY KEY NOT NULL,
  KEY `bookingID` (`bookingID`),
  CONSTRAINT `NUMOFNIGHTS_ibfk_1` FOREIGN KEY (`bookingID`) REFERENCES `BOOKING` (`bookingID`),
  CONSTRAINT `NUMOFNIGHTS_chk_1` CHECK ((`numofnights` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NUMOFNIGHTS`
--

LOCK TABLES `NUMOFNIGHTS` WRITE;
/*!40000 ALTER TABLE `NUMOFNIGHTS` DISABLE KEYS */;
/*!40000 ALTER TABLE `NUMOFNIGHTS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PAYMENT`
--

DROP TABLE IF EXISTS `PAYMENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `PAYMENT` (
  `bookingID` int NOT NULL,
  `mode` varchar(10) NOT NULL,
  `payment` int NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`bookingID`),
  CONSTRAINT `PAYMENT_ibfk_1` FOREIGN KEY (`bookingID`) REFERENCES `BOOKING` (`bookingID`),
  CONSTRAINT `check_status` CHECK ((`status` in (_utf8mb4'paid',_utf8mb4'unpaid'))),
  CONSTRAINT `PAYMENT_chk_1` CHECK ((`payment` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PAYMENT`
--

LOCK TABLES `PAYMENT` WRITE;
/*!40000 ALTER TABLE `PAYMENT` DISABLE KEYS */;
/*!40000 ALTER TABLE `PAYMENT` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `RECSERVICE`
--

DROP TABLE IF EXISTS `RECSERVICE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RECSERVICE` (
  `serviceID` int NOT NULL,
  `activityType` varchar(30) NOT NULL,
  `numPeople` int NOT NULL,
  PRIMARY KEY (`serviceID`),
  CONSTRAINT `RECSERVICE_ibfk_1` FOREIGN KEY (`serviceID`) REFERENCES `SERVICE` (`serviceID`),
  CONSTRAINT `RECSERVICE_chk_1` CHECK ((`numPeople` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RECSERVICE`
--

LOCK TABLES `RECSERVICE` WRITE;
/*!40000 ALTER TABLE `RECSERVICE` DISABLE KEYS */;
/*!40000 ALTER TABLE `RECSERVICE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESTAURANT`
--

DROP TABLE IF EXISTS `RESTAURANT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `RESTAURANT` (
  `serviceID` int NOT NULL,
  `dishCode` int NOT NULL,
  `specialRequest` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`serviceID`),
  CONSTRAINT `RESTAURANT_ibfk_1` FOREIGN KEY (`serviceID`) REFERENCES `SERVICE` (`serviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESTAURANT`
--

LOCK TABLES `RESTAURANT` WRITE;
/*!40000 ALTER TABLE `RESTAURANT` DISABLE KEYS */;
/*!40000 ALTER TABLE `RESTAURANT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ROOMCLASS`
--

DROP TABLE IF EXISTS `ROOMCLASS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ROOMCLASS` (
  `roomType` varchar(10) NOT NULL,
  `pricePerNight` int NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`roomType`),
  CONSTRAINT `ROOMCLASS_chk_1` CHECK ((`pricePerNight` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ROOMCLASS`
--

LOCK TABLES `ROOMCLASS` WRITE;
/*!40000 ALTER TABLE `ROOMCLASS` DISABLE KEYS */;
INSERT INTO `ROOMCLASS` VALUES ('standard',434,'good'),('deluxe',690,'better'),('suite',6969,'best');
/*!40000 ALTER TABLE `ROOMCLASS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ROOM`
--

DROP TABLE IF EXISTS `ROOM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ROOM` (
  `roomNo` int NOT NULL,
  `roomType` varchar(10) NOT NULL,
  `bookingID` int,
  PRIMARY KEY (`roomNo`),
  KEY `bookingID` (`bookingID`),
  KEY `roomType` (`roomType`),
  CONSTRAINT `ROOM_ibfk_1` FOREIGN KEY (`bookingID`) REFERENCES `BOOKING` (`bookingID`),
  CONSTRAINT `ROOM_ibfk_2` FOREIGN KEY (`roomType`) REFERENCES `ROOMCLASS` (`roomType`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ROOM`
--

LOCK TABLES `ROOM` WRITE;
/*!40000 ALTER TABLE `ROOM` DISABLE KEYS */;
INSERT INTO `ROOM` VALUES (1,'standard',NULL),(2,'standard',NULL),(3,'standard',NULL),(4,'standard',NULL),(5,'deluxe',NULL),(6,'deluxe',NULL),(7,'deluxe',NULL),(8,'deluxe',NULL),(9,'suite',NULL),(10,'suite',NULL),(11,'suite',NULL),(12,'suite',NULL);
/*!40000 ALTER TABLE `ROOM` ENABLE KEYS */;
UNLOCK TABLES;



--
-- Table structure for table `SERVICE`
--

DROP TABLE IF EXISTS `SERVICE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `SERVICE` (
  `serviceID` int NOT NULL,
  `roomNo` int NOT NULL,
  `servicePrice` int NOT NULL,
  PRIMARY KEY (`serviceID`),
  KEY `roomNo` (`roomNo`),
  CONSTRAINT `SERVICE_ibfk_1` FOREIGN KEY (`roomNo`) REFERENCES `ROOM` (`roomNo`),
  CONSTRAINT `SERVICE_chk_1` CHECK ((`servicePrice` > 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SERVICE`
--

LOCK TABLES `SERVICE` WRITE;
/*!40000 ALTER TABLE `SERVICE` DISABLE KEYS */;
/*!40000 ALTER TABLE `SERVICE` ENABLE KEYS */;
UNLOCK TABLES;


/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-24 19:56:38
