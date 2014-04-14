-- MySQL dump 10.13  Distrib 5.5.35, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: terpbooks
-- ------------------------------------------------------
-- Server version	5.5.35-0ubuntu0.12.04.2

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add migration history',7,'add_migrationhistory'),(20,'Can change migration history',7,'change_migrationhistory'),(21,'Can delete migration history',7,'delete_migrationhistory'),(22,'Can add semester',8,'add_semester'),(23,'Can change semester',8,'change_semester'),(24,'Can delete semester',8,'delete_semester'),(25,'Can add professor',9,'add_professor'),(26,'Can change professor',9,'change_professor'),(27,'Can delete professor',9,'delete_professor'),(28,'Can add textbook',10,'add_textbook'),(29,'Can change textbook',10,'change_textbook'),(30,'Can delete textbook',10,'delete_textbook'),(31,'Can add author',11,'add_author'),(32,'Can change author',11,'change_author'),(33,'Can delete author',11,'delete_author'),(34,'Can add listing',12,'add_listing'),(35,'Can change listing',12,'change_listing'),(36,'Can delete listing',12,'delete_listing'),(37,'Can add transaction request thread',13,'add_transactionrequestthread'),(38,'Can change transaction request thread',13,'change_transactionrequestthread'),(39,'Can delete transaction request thread',13,'delete_transactionrequestthread'),(40,'Can add transaction request',14,'add_transactionrequest'),(41,'Can change transaction request',14,'change_transactionrequest'),(42,'Can delete transaction request',14,'delete_transactionrequest');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$TOuBjGOgUxqN$hcDjlZke07ChW++pPgY5GGXDcMHOoU3s0+Oy6TVQsIA=','2014-04-14 04:58:40',1,'admin','','','',1,1,'2014-04-08 16:55:08'),(2,'pbkdf2_sha256$12000$ae9ZVZsVXWqE$kqQdHMWnbM/XuFlsI2iq5syrQ8WcK3uVw6BUxvmHppQ=','2014-04-08 16:55:16',0,'user1','','','',1,1,'2014-04-08 16:55:16'),(3,'pbkdf2_sha256$12000$Jy41ayj8jnIG$9W63nuwiWnkThYRa+dpSvK0iGnpH9tX87/tfFl8Cb0w=','2014-04-14 04:57:58',0,'user2','','','',1,1,'2014-04-08 16:55:16');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_author`
--

DROP TABLE IF EXISTS `books_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `book_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `first_name` (`first_name`,`last_name`,`book_id`),
  KEY `books_author_36c249d7` (`book_id`),
  CONSTRAINT `book_id_refs_id_eaea90d6` FOREIGN KEY (`book_id`) REFERENCES `books_textbook` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_author`
--

LOCK TABLES `books_author` WRITE;
/*!40000 ALTER TABLE `books_author` DISABLE KEYS */;
INSERT INTO `books_author` VALUES (1,'Bob','Doe',1),(4,'Bob','Doe',2),(7,'Bob','Doe',3),(10,'Bob','Doe',4),(11,'Bob','Doe',5),(12,'Bob','Doe',6),(13,'Bob','Doe',7),(16,'Bob','Doe',8),(18,'Bob','Doe',9),(19,'Bob','Doe',10),(20,'Bob','Doe',11),(21,'Bob','Doe',12),(24,'Bob','Doe',13),(27,'Bob','Doe',14),(30,'Bob','Doe',15),(31,'Bob','Doe',16),(2,'Bob','Grant',1),(5,'Bob','Grant',2),(8,'Bob','Grant',3),(14,'Bob','Grant',7),(17,'Bob','Grant',8),(22,'Bob','Grant',12),(25,'Bob','Grant',13),(28,'Bob','Grant',14),(3,'Bob','Gray',1),(6,'Bob','Gray',2),(9,'Bob','Gray',3),(15,'Bob','Gray',7),(23,'Bob','Gray',12),(26,'Bob','Gray',13),(29,'Bob','Gray',14);
/*!40000 ALTER TABLE `books_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_professor`
--

DROP TABLE IF EXISTS `books_professor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_professor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `first_name` (`first_name`,`last_name`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_professor`
--

LOCK TABLES `books_professor` WRITE;
/*!40000 ALTER TABLE `books_professor` DISABLE KEYS */;
INSERT INTO `books_professor` VALUES (4,'Bob','Brown'),(1,'Bob','Doe'),(2,'Bob','Grant'),(3,'Bob','Gray'),(12,'Jane','Brown'),(9,'Jane','Doe'),(10,'Jane','Grant'),(11,'Jane','Gray'),(8,'John','Brown'),(5,'John','Doe'),(6,'John','Grant'),(7,'John','Gray'),(16,'Sally','Brown'),(13,'Sally','Doe'),(14,'Sally','Grant'),(15,'Sally','Gray');
/*!40000 ALTER TABLE `books_professor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_semester`
--

DROP TABLE IF EXISTS `books_semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_semester` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL,
  `semester` varchar(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `year` (`year`,`semester`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_semester`
--

LOCK TABLES `books_semester` WRITE;
/*!40000 ALTER TABLE `books_semester` DISABLE KEYS */;
INSERT INTO `books_semester` VALUES (9,2011,'ASP'),(13,2011,'BSM'),(1,2011,'CFL'),(5,2011,'DWN'),(10,2012,'ASP'),(14,2012,'BSM'),(2,2012,'CFL'),(6,2012,'DWN'),(11,2013,'ASP'),(15,2013,'BSM'),(3,2013,'CFL'),(7,2013,'DWN'),(12,2014,'ASP'),(16,2014,'BSM'),(4,2014,'CFL'),(8,2014,'DWN');
/*!40000 ALTER TABLE `books_semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books_textbook`
--

DROP TABLE IF EXISTS `books_textbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books_textbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL,
  `edition` int(11) DEFAULT NULL,
  `isbn` varchar(13) NOT NULL,
  `course_code` varchar(20) NOT NULL,
  `semester_id` int(11) DEFAULT NULL,
  `professor_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `books_textbook_7ce38e1e` (`semester_id`),
  KEY `books_textbook_b9498a38` (`professor_id`),
  CONSTRAINT `semester_id_refs_id_311fc002` FOREIGN KEY (`semester_id`) REFERENCES `books_semester` (`id`),
  CONSTRAINT `professor_id_refs_id_a2f41842` FOREIGN KEY (`professor_id`) REFERENCES `books_professor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_textbook`
--

LOCK TABLES `books_textbook` WRITE;
/*!40000 ALTER TABLE `books_textbook` DISABLE KEYS */;
INSERT INTO `books_textbook` VALUES (1,'A History of Physics',1,'4537239203655','CMSC101',1,1),(2,'A History of Technical Writing',2,'7346540103530','CMSC201',2,2),(3,'A History of Calculus',1,'4061773408573','CMSC301',3,3),(4,'A History of Algorithms',1,'0786216959808','CMSC401',4,4),(5,'General Background of Physics',1,'5763948366923','PHYS101',5,5),(6,'General Background of Technical Writing',1,'4302043539078','PHYS201',6,6),(7,'General Background of Calculus',3,'9745267357440','PHYS301',7,7),(8,'General Background of Algorithms',3,'7883017156409','PHYS401',8,8),(9,'Beginner\'s Guide to Physics',2,'9333914774210','MATH101',9,9),(10,'Beginner\'s Guide to Technical Writing',3,'4454544228233','MATH201',10,10),(11,'Beginner\'s Guide to Calculus',1,'2572724025124','MATH301',11,11),(12,'Beginner\'s Guide to Algorithms',2,'2217372447314','MATH401',12,12),(13,'Become an Expert in Physics',3,'7819985138034','ENGL101',13,13),(14,'Become an Expert in Technical Writing',1,'8015839829586','ENGL201',14,14),(15,'Become an Expert in Calculus',1,'1610147052570','ENGL301',15,15),(16,'Become an Expert in Algorithms',1,'6770096315863','ENGL401',16,16);
/*!40000 ALTER TABLE `books_textbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-04-08 16:56:39',1,12,'1','A History of Physics: Available',2,'Changed owner.'),(2,'2014-04-08 16:56:46',1,12,'4','A History of Algorithms: Available',2,'Changed owner.'),(3,'2014-04-10 00:56:43',1,13,'1','A History of Physics',2,'Added transaction request \"TransactionRequest object\".'),(4,'2014-04-10 01:20:23',1,13,'1','A History of Physics',2,'Changed text for transaction request \"TransactionRequest object\".'),(5,'2014-04-10 03:22:04',1,4,'3','user2',2,'Changed is_staff.'),(6,'2014-04-10 03:22:36',1,4,'1','admin',2,'Changed password.'),(7,'2014-04-10 03:22:39',1,4,'3','user2',2,'No fields changed.'),(8,'2014-04-14 04:35:41',1,13,'17','Become an Expert in Calculus',1,''),(9,'2014-04-14 04:57:08',1,4,'1','admin',2,'Changed password.'),(10,'2014-04-14 04:57:15',1,4,'2','user1',2,'Changed is_staff.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'migration history','south','migrationhistory'),(8,'semester','books','semester'),(9,'professor','books','professor'),(10,'textbook','books','textbook'),(11,'author','books','author'),(12,'listing','transactions','listing'),(13,'transaction request thread','transactions','transactionrequestthread'),(14,'transaction request','transactions','transactionrequest');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('smu7pk1g05lz0uip31ieinrix3csm572','ZDgzNTBjOGI0NjllNjc1YTE4ZWUxMjFiYTkyNGZmZTZkYjdkN2FiYzp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-04-28 04:58:40');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions_listing`
--

DROP TABLE IF EXISTS `transactions_listing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions_listing` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_created` date NOT NULL,
  `status` varchar(2) NOT NULL,
  `asking_price` decimal(10,2) NOT NULL,
  `owner_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `comments` longtext NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `book_id` (`book_id`),
  KEY `transactions_listing_cb902d83` (`owner_id`),
  CONSTRAINT `book_id_refs_id_005210c8` FOREIGN KEY (`book_id`) REFERENCES `books_textbook` (`id`),
  CONSTRAINT `owner_id_refs_id_a4dfc442` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_listing`
--

LOCK TABLES `transactions_listing` WRITE;
/*!40000 ALTER TABLE `transactions_listing` DISABLE KEYS */;
INSERT INTO `transactions_listing` VALUES (1,'2014-04-08','AV',5.54,1,1,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(2,'2014-04-08','SD',0.48,3,2,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(3,'2014-04-08','PN',4.05,2,3,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(4,'2014-04-08','AV',1.82,1,4,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(5,'2014-04-08','PN',6.14,2,5,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(6,'2014-04-08','AV',7.44,3,6,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(7,'2014-04-08','PN',5.72,2,7,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(8,'2014-04-08','AV',1.12,3,8,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(9,'2014-04-08','PN',5.42,2,9,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(10,'2014-04-08','AV',6.11,3,10,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(11,'2014-04-08','SD',3.94,2,11,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(12,'2014-04-08','PN',6.83,3,12,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(13,'2014-04-08','PN',0.56,2,13,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(14,'2014-04-08','SD',8.04,3,14,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(15,'2014-04-08','AV',7.86,2,15,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(16,'2014-04-08','SD',8.34,3,16,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
/*!40000 ALTER TABLE `transactions_listing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions_transactionrequest`
--

DROP TABLE IF EXISTS `transactions_transactionrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions_transactionrequest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_by_id` int(11) NOT NULL,
  `date_created` datetime NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `text` longtext NOT NULL,
  `read` tinyint(1) NOT NULL,
  `thread_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transactions_transactionrequest_0c98d849` (`created_by_id`),
  KEY `transactions_transactionrequest_bd1a2e3a` (`thread_id`),
  CONSTRAINT `created_by_id_refs_id_5489323b` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `thread_id_refs_id_d88a8a39` FOREIGN KEY (`thread_id`) REFERENCES `transactions_transactionrequestthread` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_transactionrequest`
--

LOCK TABLES `transactions_transactionrequest` WRITE;
/*!40000 ALTER TABLE `transactions_transactionrequest` DISABLE KEYS */;
INSERT INTO `transactions_transactionrequest` VALUES (1,3,'2014-04-08 16:55:16',2.38,'Sed elementum est eget nibh venenatis vestibulum.',1,1),(2,2,'2014-04-08 16:55:16',0.28,'Sed elementum est eget nibh venenatis vestibulum.',1,2),(3,3,'2014-04-08 16:55:16',0.67,'Sed elementum est eget nibh venenatis vestibulum.',0,3),(4,2,'2014-04-08 16:55:16',0.23,'Sed elementum est eget nibh venenatis vestibulum.',0,3),(5,3,'2014-04-08 16:55:16',3.80,'Sed elementum est eget nibh venenatis vestibulum.',0,3),(6,2,'2014-04-08 16:55:16',1.79,'Sed elementum est eget nibh venenatis vestibulum.',1,4),(7,3,'2014-04-08 16:55:16',4.54,'Sed elementum est eget nibh venenatis vestibulum.',0,5),(8,2,'2014-04-08 16:55:16',5.00,'Sed elementum est eget nibh venenatis vestibulum.',0,5),(9,3,'2014-04-08 16:55:16',2.20,'Sed elementum est eget nibh venenatis vestibulum.',0,5),(10,2,'2014-04-08 16:55:16',1.54,'Sed elementum est eget nibh venenatis vestibulum.',0,5),(11,2,'2014-04-08 16:55:16',0.80,'Sed elementum est eget nibh venenatis vestibulum.',0,6),(12,3,'2014-04-08 16:55:16',2.50,'Sed elementum est eget nibh venenatis vestibulum.',0,7),(13,2,'2014-04-08 16:55:16',2.09,'Sed elementum est eget nibh venenatis vestibulum.',0,7),(14,3,'2014-04-08 16:55:16',5.47,'Sed elementum est eget nibh venenatis vestibulum.',0,7),(15,2,'2014-04-08 16:55:16',0.97,'Sed elementum est eget nibh venenatis vestibulum.',0,8),(16,3,'2014-04-08 16:55:16',0.65,'Sed elementum est eget nibh venenatis vestibulum.',0,8),(17,2,'2014-04-08 16:55:16',0.74,'Sed elementum est eget nibh venenatis vestibulum.',0,8),(18,3,'2014-04-08 16:55:16',0.22,'Sed elementum est eget nibh venenatis vestibulum.',0,9),(19,2,'2014-04-08 16:55:16',4.92,'Sed elementum est eget nibh venenatis vestibulum.',1,10),(20,3,'2014-04-08 16:55:16',4.53,'Sed elementum est eget nibh venenatis vestibulum.',0,10),(21,2,'2014-04-08 16:55:16',4.97,'Sed elementum est eget nibh venenatis vestibulum.',1,10),(22,3,'2014-04-08 16:55:16',1.70,'Sed elementum est eget nibh venenatis vestibulum.',0,11),(23,2,'2014-04-08 16:55:16',1.39,'Sed elementum est eget nibh venenatis vestibulum.',0,11),(24,3,'2014-04-08 16:55:16',2.30,'Sed elementum est eget nibh venenatis vestibulum.',0,11),(25,2,'2014-04-08 16:55:16',1.95,'Sed elementum est eget nibh venenatis vestibulum.',0,11),(26,2,'2014-04-08 16:55:16',6.44,'Sed elementum est eget nibh venenatis vestibulum.',1,12),(27,3,'2014-04-08 16:55:16',1.33,'Sed elementum est eget nibh venenatis vestibulum.',0,12),(28,3,'2014-04-08 16:55:16',0.17,'Sed elementum est eget nibh venenatis vestibulum.',0,13),(29,2,'2014-04-08 16:55:16',0.20,'Sed elementum est eget nibh venenatis vestibulum.',0,13),(30,3,'2014-04-08 16:55:16',0.12,'Sed elementum est eget nibh venenatis vestibulum.',0,13),(31,2,'2014-04-08 16:55:17',6.20,'Sed elementum est eget nibh venenatis vestibulum.',1,14),(32,3,'2014-04-08 16:55:17',2.13,'Sed elementum est eget nibh venenatis vestibulum.',0,14),(33,2,'2014-04-08 16:55:17',1.06,'Sed elementum est eget nibh venenatis vestibulum.',1,14),(34,3,'2014-04-08 16:55:17',0.89,'Sed elementum est eget nibh venenatis vestibulum.',0,15),(35,2,'2014-04-08 16:55:17',3.42,'Sed elementum est eget nibh venenatis vestibulum.',0,15),(36,2,'2014-04-08 16:55:17',4.45,'Sed elementum est eget nibh venenatis vestibulum.',1,16),(37,3,'2014-04-08 16:55:17',5.14,'Sed elementum est eget nibh venenatis vestibulum.',0,16),(38,2,'2014-04-08 16:55:17',6.34,'Sed elementum est eget nibh venenatis vestibulum.',1,16),(39,1,'2014-04-10 00:56:43',5.02,'LOL bro wtf u trying to say????? In hac habitasse platea dictumst. Mauris iaculis eleifend enim, sed malesuada felis pharetra eu. Praesent pretium aliquam mi ut accumsan. Sed sed est non ipsum sodales euismod. Nam hendrerit ac enim ac bibendum. Etiam aliquet vehicula nunc, vitae iaculis orci ultricies vitae. Mauris at gravida sapien.',0,1),(40,1,'2014-04-10 02:42:32',1.00,'test',0,1),(41,1,'2014-04-10 02:45:55',3.00,'Test2',0,1),(42,1,'2014-04-10 02:46:26',1.00,'test3',0,1),(43,1,'2014-04-10 02:52:08',2.00,'test4',0,1),(44,1,'2014-04-10 02:57:54',0.01,'test5',0,1),(45,1,'2014-04-10 03:00:48',0.01,'test6',0,1),(46,1,'2014-04-10 03:01:47',2.00,'test7',0,1),(47,1,'2014-04-14 04:35:41',1.00,'YOLOSWAG420',0,17),(48,1,'2014-04-14 05:12:41',2.00,'Message 2',0,17),(49,1,'2014-04-14 05:12:54',2.00,'Message 2',0,17),(50,1,'2014-04-14 05:13:55',2.10,'Message 4',0,17);
/*!40000 ALTER TABLE `transactions_transactionrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions_transactionrequestthread`
--

DROP TABLE IF EXISTS `transactions_transactionrequestthread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions_transactionrequestthread` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `date_created` datetime NOT NULL,
  `listing_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transactions_transactionrequestthread_0a681a64` (`sender_id`),
  KEY `transactions_transactionrequestthread_cc7968a2` (`listing_id`),
  CONSTRAINT `listing_id_refs_id_09a7f81e` FOREIGN KEY (`listing_id`) REFERENCES `transactions_listing` (`id`),
  CONSTRAINT `sender_id_refs_id_aa82fd1b` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_transactionrequestthread`
--

LOCK TABLES `transactions_transactionrequestthread` WRITE;
/*!40000 ALTER TABLE `transactions_transactionrequestthread` DISABLE KEYS */;
INSERT INTO `transactions_transactionrequestthread` VALUES (1,3,'2014-04-08 16:55:16',1),(2,2,'2014-04-08 16:55:16',2),(3,3,'2014-04-08 16:55:16',3),(4,2,'2014-04-08 16:55:16',4),(5,3,'2014-04-08 16:55:16',5),(6,2,'2014-04-08 16:55:16',6),(7,3,'2014-04-08 16:55:16',7),(8,2,'2014-04-08 16:55:16',8),(9,3,'2014-04-08 16:55:16',9),(10,2,'2014-04-08 16:55:16',10),(11,3,'2014-04-08 16:55:16',11),(12,2,'2014-04-08 16:55:16',12),(13,3,'2014-04-08 16:55:16',13),(14,2,'2014-04-08 16:55:17',14),(15,3,'2014-04-08 16:55:17',15),(16,2,'2014-04-08 16:55:17',16),(17,1,'2014-04-14 04:35:41',15);
/*!40000 ALTER TABLE `transactions_transactionrequestthread` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-14  5:19:00
