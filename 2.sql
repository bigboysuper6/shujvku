-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: people
-- ------------------------------------------------------
-- Server version	5.7.34-log

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
-- Table structure for table `dangan`
--

DROP TABLE IF EXISTS `dangan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dangan` (
  `dangan_id` int(11) NOT NULL AUTO_INCREMENT,
  `dangan_no` char(50) DEFAULT NULL,
  `l_name` varchar(50) NOT NULL,
  `ll_name` varchar(50) NOT NULL,
  `lll_name` varchar(50) NOT NULL,
  `zwfl` varchar(50) NOT NULL,
  `zwmc` varchar(50) NOT NULL,
  `zc` varchar(50) DEFAULT NULL,
  `xm` varchar(50) NOT NULL,
  `xb` varchar(2) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dh` varchar(50) NOT NULL,
  `qq` varchar(50) NOT NULL,
  `sj` varchar(50) NOT NULL,
  `zz` varchar(50) NOT NULL,
  `yb` varchar(50) NOT NULL,
  `gj` varchar(50) NOT NULL,
  `csd` varchar(50) NOT NULL,
  `sr` varchar(50) NOT NULL,
  `mz` varchar(50) NOT NULL,
  `zj` varchar(50) NOT NULL,
  `zzmm` varchar(50) NOT NULL,
  `sfzh` varchar(50) NOT NULL,
  `sbhm` varchar(50) NOT NULL,
  `nl` int(11) NOT NULL,
  `xl` varchar(50) NOT NULL,
  `jynx` int(11) NOT NULL,
  `xlzy` varchar(50) NOT NULL,
  `xcbz` varchar(50) NOT NULL,
  `khh` varchar(50) NOT NULL,
  `khzh` varchar(50) NOT NULL,
  `djr` varchar(50) DEFAULT NULL,
  `djsj` varchar(50) DEFAULT NULL,
  `tc` varchar(50) NOT NULL,
  `ah` varchar(50) NOT NULL,
  `grll` varchar(300) DEFAULT NULL,
  `jtgx` varchar(300) DEFAULT NULL,
  `bz` varchar(300) DEFAULT NULL,
  `dazt` varchar(10) DEFAULT '待审核',
  PRIMARY KEY (`dangan_id`),
  UNIQUE KEY `dangan_no` (`dangan_no`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dangan`
--

LOCK TABLES `dangan` WRITE;
/*!40000 ALTER TABLE `dangan` DISABLE KEYS */;
INSERT INTO `dangan` VALUES (26,'2019-01-01-01-01','集团一','软件公司','软件编译','员工','普通员工','普通员工','温杰','男','785273865@qq.com','14715911111','785273865','785273865','海大','514700','中国','广东梅州','1997.09.18','汉族','佛','群众','441421111111111111','001',21,'本科',12,'计算机','员工','建设','001','wjp1','2019-01-27','python','音乐','无\n\n\n\n\n','无\n\n\n\n\n','无\n\n\n\n\n','daishenhe');
/*!40000 ALTER TABLE `dangan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `l_itt`
--

DROP TABLE IF EXISTS `l_itt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `l_itt` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_itt_no` varchar(2) DEFAULT NULL,
  `l_itt_name` varchar(50) NOT NULL,
  PRIMARY KEY (`l_id`),
  UNIQUE KEY `l_itt_no` (`l_itt_no`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `l_itt`
--

LOCK TABLES `l_itt` WRITE;
/*!40000 ALTER TABLE `l_itt` DISABLE KEYS */;
INSERT INTO `l_itt` VALUES (1,'01','集团一'),(2,'02','集团二');
/*!40000 ALTER TABLE `l_itt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ll_itt`
--

DROP TABLE IF EXISTS `ll_itt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ll_itt` (
  `ll_id` int(11) NOT NULL AUTO_INCREMENT,
  `ll_itt_no` varchar(2) DEFAULT NULL,
  `ll_itt_name` varchar(50) NOT NULL,
  `ll_bl_l` varchar(2) NOT NULL,
  PRIMARY KEY (`ll_id`),
  UNIQUE KEY `ll_itt_no` (`ll_itt_no`),
  KEY `ll_bl_l` (`ll_bl_l`),
  CONSTRAINT `ll_itt_ibfk_1` FOREIGN KEY (`ll_bl_l`) REFERENCES `l_itt` (`l_itt_no`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ll_itt`
--

LOCK TABLES `ll_itt` WRITE;
/*!40000 ALTER TABLE `ll_itt` DISABLE KEYS */;
INSERT INTO `ll_itt` VALUES (1,'01','软件公司','01'),(2,'02','硬件公司','01'),(3,'03','模具公司','02'),(4,'04','包装公司','02');
/*!40000 ALTER TABLE `ll_itt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lll_itt`
--

DROP TABLE IF EXISTS `lll_itt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lll_itt` (
  `lll_id` int(11) NOT NULL AUTO_INCREMENT,
  `lll_itt_no` varchar(2) DEFAULT NULL,
  `lll_itt_name` varchar(50) NOT NULL,
  `lll_bl_ll` varchar(2) NOT NULL,
  PRIMARY KEY (`lll_id`),
  UNIQUE KEY `lll_itt_no` (`lll_itt_no`),
  KEY `lll_bl_ll` (`lll_bl_ll`),
  CONSTRAINT `lll_itt_ibfk_1` FOREIGN KEY (`lll_bl_ll`) REFERENCES `ll_itt` (`ll_itt_no`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lll_itt`
--

LOCK TABLES `lll_itt` WRITE;
/*!40000 ALTER TABLE `lll_itt` DISABLE KEYS */;
INSERT INTO `lll_itt` VALUES (1,'01','软件编译','01'),(2,'02','软件测试','01'),(3,'03','硬件生产','02'),(4,'04','硬件测试','02'),(5,'05','模具生产','03'),(6,'06','模具测试','03'),(7,'07','包装生产','04'),(8,'08','包装测试','04');
/*!40000 ALTER TABLE `lll_itt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_name` varchar(50) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_aut` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('111111','111111','人事专员'),('123','123456','人事经理'),('222222','222222','人事经理'),('444444','444444','薪酬经理'),('wjp1','05091117','人事经理'),('wjp2','05091117','人事专员');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xcxm`
--

DROP TABLE IF EXISTS `xcxm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `xcxm` (
  `xcbzbh` varchar(45) NOT NULL,
  `xcbzmc` varchar(45) DEFAULT NULL,
  `zdr` varchar(45) DEFAULT NULL,
  `djsj` varchar(45) DEFAULT NULL,
  `zwmc` varchar(45) DEFAULT NULL,
  `jbgz` varchar(45) DEFAULT NULL,
  `yanglbx` varchar(45) DEFAULT NULL,
  `ylbx` varchar(45) DEFAULT NULL,
  `sybx` varchar(45) DEFAULT NULL,
  `zfgjj` varchar(45) DEFAULT NULL,
  `zt` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`xcbzbh`),
  UNIQUE KEY `xcxmbh_UNIQUE` (`xcbzbh`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xcxm`
--

LOCK TABLES `xcxm` WRITE;
/*!40000 ALTER TABLE `xcxm` DISABLE KEYS */;
INSERT INTO `xcxm` VALUES ('1','1','1','2021-07-03','1','1','1','1','1','1','fuhe'),('2','2','2','2021-07-03','2','2','2','2','2','2','fuhe'),('3','3','3','2021-07-03','3','3','3','3','3','3','fuhe'),('4','4','4','2021-07-03','4','4','4','4','4','3','yifuhe'),('5','5','5','2021-07-03','5','5','5','5','5','5','yifuhe'),('6','6','6','2021-07-03','6','6','6','6','6','6','fuhe');
/*!40000 ALTER TABLE `xcxm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ygxc`
--

DROP TABLE IF EXISTS `ygxc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ygxc` (
  `ygbh` varchar(45) NOT NULL,
  `jljj` varchar(45) DEFAULT NULL,
  `kcjj` varchar(45) DEFAULT NULL,
  `yfze` varchar(45) DEFAULT NULL,
  `xcbzbh` varchar(45) DEFAULT NULL,
  `djr` varchar(45) DEFAULT NULL,
  `zt` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ygbh`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ygxc`
--

LOCK TABLES `ygxc` WRITE;
/*!40000 ALTER TABLE `ygxc` DISABLE KEYS */;
INSERT INTO `ygxc` VALUES ('1','1','1','1','1','1','daifuhe'),('3','3','3','3','3','3','daidengji');
/*!40000 ALTER TABLE `ygxc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-04 18:30:37
