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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add message thread',7,'add_messagethread'),(20,'Can change message thread',7,'change_messagethread'),(21,'Can delete message thread',7,'delete_messagethread'),(22,'Can add message',8,'add_message'),(23,'Can change message',8,'change_message'),(24,'Can delete message',8,'delete_message'),(25,'Can add migration history',9,'add_migrationhistory'),(26,'Can change migration history',9,'change_migrationhistory'),(27,'Can delete migration history',9,'delete_migrationhistory'),(28,'Can add semester',10,'add_semester'),(29,'Can change semester',10,'change_semester'),(30,'Can delete semester',10,'delete_semester'),(31,'Can add professor',11,'add_professor'),(32,'Can change professor',11,'change_professor'),(33,'Can delete professor',11,'delete_professor'),(34,'Can add textbook',12,'add_textbook'),(35,'Can change textbook',12,'change_textbook'),(36,'Can delete textbook',12,'delete_textbook'),(37,'Can add author',13,'add_author'),(38,'Can change author',13,'change_author'),(39,'Can delete author',13,'delete_author'),(40,'Can add listing',14,'add_listing'),(41,'Can change listing',14,'change_listing'),(42,'Can delete listing',14,'delete_listing'),(43,'Can add transaction request thread',15,'add_transactionrequestthread'),(44,'Can change transaction request thread',15,'change_transactionrequestthread'),(45,'Can delete transaction request thread',15,'delete_transactionrequestthread'),(46,'Can add transaction request',16,'add_transactionrequest'),(47,'Can change transaction request',16,'change_transactionrequest'),(48,'Can delete transaction request',16,'delete_transactionrequest');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$v36NvYOpOufT$zu8k6M4YemY/pD1db589FTmhVtTKZG/xb7Txjj+qYyk=','2014-03-31 19:46:38',1,'admin','','','',1,1,'2014-03-31 19:46:38'),(2,'pbkdf2_sha256$12000$1UsgRfN3RQ3d$I9s0u03+7dXsMnRJJrryteDF0GiSp2gCH/LudK9Q2U4=','2014-03-31 19:46:46',0,'user1','','','',0,1,'2014-03-31 19:46:46'),(3,'pbkdf2_sha256$12000$5XteDOSMVqxd$sOcwPAJM6Ol/KOa5mpUKDKlAHK1s0E3RLMSJQooLA4A=','2014-03-31 19:46:46',0,'user2','','','',0,1,'2014-03-31 19:46:46');
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
  KEY `books_author_36c249d7` (`book_id`),
  CONSTRAINT `book_id_refs_id_eaea90d6` FOREIGN KEY (`book_id`) REFERENCES `books_textbook` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_author`
--

LOCK TABLES `books_author` WRITE;
/*!40000 ALTER TABLE `books_author` DISABLE KEYS */;
INSERT INTO `books_author` VALUES (1,'Bob','Doe',1),(2,'Bob','Grant',1),(3,'Bob','Doe',2),(4,'Bob','Doe',3),(5,'Bob','Grant',3),(6,'Bob','Gray',3),(7,'Bob','Doe',4),(8,'Bob','Grant',4),(9,'Bob','Gray',4),(10,'Bob','Doe',5),(11,'Bob','Doe',6),(12,'Bob','Grant',6),(13,'Bob','Doe',7),(14,'Bob','Grant',7),(15,'Bob','Doe',8),(16,'Bob','Grant',8),(17,'Bob','Gray',8),(18,'Bob','Doe',9),(19,'Bob','Grant',9),(20,'Bob','Doe',10),(21,'Bob','Grant',10),(22,'Bob','Doe',11),(23,'Bob','Grant',11),(24,'Bob','Gray',11),(25,'Bob','Doe',12),(26,'Bob','Grant',12),(27,'Bob','Doe',13),(28,'Bob','Doe',14),(29,'Bob','Grant',14),(30,'Bob','Gray',14),(31,'Bob','Doe',15),(32,'Bob','Grant',15),(33,'Bob','Gray',15),(34,'Bob','Doe',16),(35,'Bob','Grant',16),(36,'Bob','Gray',16);
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
  CONSTRAINT `professor_id_refs_id_a2f41842` FOREIGN KEY (`professor_id`) REFERENCES `books_professor` (`id`),
  CONSTRAINT `semester_id_refs_id_311fc002` FOREIGN KEY (`semester_id`) REFERENCES `books_semester` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books_textbook`
--

LOCK TABLES `books_textbook` WRITE;
/*!40000 ALTER TABLE `books_textbook` DISABLE KEYS */;
INSERT INTO `books_textbook` VALUES (1,'A History of Physics',3,'9086119559474','CMSC101',1,1),(2,'A History of Technical Writing',3,'2322269445564','CMSC201',2,2),(3,'A History of Calculus',3,'7073780419073','CMSC301',3,3),(4,'A History of Algorithms',1,'7925361378937','CMSC401',4,4),(5,'General Background of Physics',3,'5708033104134','PHYS101',5,5),(6,'General Background of Technical Writing',2,'9355038468096','PHYS201',6,6),(7,'General Background of Calculus',1,'8504090340105','PHYS301',7,7),(8,'General Background of Algorithms',2,'0647152308721','PHYS401',8,8),(9,'Beginner\'s Guide to Physics',1,'8295510296854','MATH101',9,9),(10,'Beginner\'s Guide to Technical Writing',2,'8202341075809','MATH201',10,10),(11,'Beginner\'s Guide to Calculus',3,'0948644221071','MATH301',11,11),(12,'Beginner\'s Guide to Algorithms',2,'6436345794067','MATH401',12,12),(13,'Become an Expert in Physics',1,'6343513470614','ENGL101',13,13),(14,'Become an Expert in Technical Writing',2,'0323457300276','ENGL201',14,14),(15,'Become an Expert in Calculus',2,'9496394924899','ENGL301',15,15),(16,'Become an Expert in Algorithms',2,'5854391023803','ENGL401',16,16);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'message thread','messages','messagethread'),(8,'message','messages','message'),(9,'migration history','south','migrationhistory'),(10,'semester','books','semester'),(11,'professor','books','professor'),(12,'textbook','books','textbook'),(13,'author','books','author'),(14,'listing','transactions','listing'),(15,'transaction request thread','transactions','transactionrequestthread'),(16,'transaction request','transactions','transactionrequest');
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages_message`
--

DROP TABLE IF EXISTS `messages_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `text` longtext NOT NULL,
  `thread_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messages_message_cb902d83` (`owner_id`),
  KEY `messages_message_bd1a2e3a` (`thread_id`),
  CONSTRAINT `thread_id_refs_id_8fd0c475` FOREIGN KEY (`thread_id`) REFERENCES `messages_messagethread` (`id`),
  CONSTRAINT `owner_id_refs_id_1c93ff62` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages_message`
--

LOCK TABLES `messages_message` WRITE;
/*!40000 ALTER TABLE `messages_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages_messagethread`
--

DROP TABLE IF EXISTS `messages_messagethread`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages_messagethread` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `recipient_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `messages_messagethread_0a681a64` (`sender_id`),
  KEY `messages_messagethread_3e31d986` (`recipient_id`),
  CONSTRAINT `recipient_id_refs_id_0d1b7384` FOREIGN KEY (`recipient_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `sender_id_refs_id_0d1b7384` FOREIGN KEY (`sender_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages_messagethread`
--

LOCK TABLES `messages_messagethread` WRITE;
/*!40000 ALTER TABLE `messages_messagethread` DISABLE KEYS */;
/*!40000 ALTER TABLE `messages_messagethread` ENABLE KEYS */;
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
INSERT INTO `transactions_listing` VALUES (1,'2014-03-31','AV',6.18,2,1,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(2,'2014-03-31','SD',4.43,3,2,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(3,'2014-03-31','SD',4.25,2,3,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(4,'2014-03-31','AV',5.53,3,4,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(5,'2014-03-31','PN',5.42,2,5,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(6,'2014-03-31','SD',5.18,3,6,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(7,'2014-03-31','SD',9.98,2,7,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(8,'2014-03-31','AV',1.76,3,8,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(9,'2014-03-31','PN',3.29,2,9,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(10,'2014-03-31','AV',9.13,3,10,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(11,'2014-03-31','AV',2.29,2,11,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(12,'2014-03-31','AV',3.40,3,12,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(13,'2014-03-31','SD',2.47,2,13,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(14,'2014-03-31','SD',6.52,3,14,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(15,'2014-03-31','PN',8.67,2,15,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),(16,'2014-03-31','SD',8.02,3,16,'Lorem ipsum dolor sit amet, consectetur adipiscing elit.');
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
  `price` decimal(10,2) NOT NULL,
  `text` longtext NOT NULL,
  `thread_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transactions_transactionrequest_0c98d849` (`created_by_id`),
  KEY `transactions_transactionrequest_bd1a2e3a` (`thread_id`),
  CONSTRAINT `thread_id_refs_id_d88a8a39` FOREIGN KEY (`thread_id`) REFERENCES `transactions_transactionrequestthread` (`id`),
  CONSTRAINT `created_by_id_refs_id_5489323b` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_transactionrequest`
--

LOCK TABLES `transactions_transactionrequest` WRITE;
/*!40000 ALTER TABLE `transactions_transactionrequest` DISABLE KEYS */;
INSERT INTO `transactions_transactionrequest` VALUES (1,3,1.69,'Sed elementum est eget nibh venenatis vestibulum.',1),(2,2,2.15,'Sed elementum est eget nibh venenatis vestibulum.',1),(3,2,0.92,'Sed elementum est eget nibh venenatis vestibulum.',2),(4,3,2.73,'Sed elementum est eget nibh venenatis vestibulum.',3),(5,2,3.24,'Sed elementum est eget nibh venenatis vestibulum.',4),(6,3,3.15,'Sed elementum est eget nibh venenatis vestibulum.',5),(7,2,5.34,'Sed elementum est eget nibh venenatis vestibulum.',5),(8,3,1.39,'Sed elementum est eget nibh venenatis vestibulum.',5),(9,2,4.39,'Sed elementum est eget nibh venenatis vestibulum.',6),(10,3,4.20,'Sed elementum est eget nibh venenatis vestibulum.',6),(11,2,3.95,'Sed elementum est eget nibh venenatis vestibulum.',6),(12,3,2.17,'Sed elementum est eget nibh venenatis vestibulum.',6),(13,3,9.56,'Sed elementum est eget nibh venenatis vestibulum.',7),(14,2,1.27,'Sed elementum est eget nibh venenatis vestibulum.',7),(15,2,1.56,'Sed elementum est eget nibh venenatis vestibulum.',8),(16,3,0.07,'Sed elementum est eget nibh venenatis vestibulum.',8),(17,2,1.56,'Sed elementum est eget nibh venenatis vestibulum.',8),(18,3,0.40,'Sed elementum est eget nibh venenatis vestibulum.',8),(19,3,2.38,'Sed elementum est eget nibh venenatis vestibulum.',9),(20,2,0.37,'Sed elementum est eget nibh venenatis vestibulum.',9),(21,3,1.00,'Sed elementum est eget nibh venenatis vestibulum.',9),(22,2,7.84,'Sed elementum est eget nibh venenatis vestibulum.',10),(23,3,2.62,'Sed elementum est eget nibh venenatis vestibulum.',10),(24,2,2.34,'Sed elementum est eget nibh venenatis vestibulum.',10),(25,3,2.00,'Sed elementum est eget nibh venenatis vestibulum.',10),(26,3,0.44,'Sed elementum est eget nibh venenatis vestibulum.',11),(27,2,2.42,'Sed elementum est eget nibh venenatis vestibulum.',12),(28,3,1.68,'Sed elementum est eget nibh venenatis vestibulum.',12),(29,2,3.09,'Sed elementum est eget nibh venenatis vestibulum.',12),(30,3,1.05,'Sed elementum est eget nibh venenatis vestibulum.',13),(31,2,1.38,'Sed elementum est eget nibh venenatis vestibulum.',13),(32,3,1.89,'Sed elementum est eget nibh venenatis vestibulum.',13),(33,2,0.35,'Sed elementum est eget nibh venenatis vestibulum.',13),(34,2,3.40,'Sed elementum est eget nibh venenatis vestibulum.',14),(35,3,0.80,'Sed elementum est eget nibh venenatis vestibulum.',14),(36,2,4.35,'Sed elementum est eget nibh venenatis vestibulum.',14),(37,3,0.32,'Sed elementum est eget nibh venenatis vestibulum.',15),(38,2,6.09,'Sed elementum est eget nibh venenatis vestibulum.',16),(39,3,6.92,'Sed elementum est eget nibh venenatis vestibulum.',16),(40,2,6.09,'Sed elementum est eget nibh venenatis vestibulum.',16),(41,3,6.29,'Sed elementum est eget nibh venenatis vestibulum.',16);
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions_transactionrequestthread`
--

LOCK TABLES `transactions_transactionrequestthread` WRITE;
/*!40000 ALTER TABLE `transactions_transactionrequestthread` DISABLE KEYS */;
INSERT INTO `transactions_transactionrequestthread` VALUES (1,3,'2014-03-31 19:46:46',1),(2,2,'2014-03-31 19:46:46',2),(3,3,'2014-03-31 19:46:46',3),(4,2,'2014-03-31 19:46:46',4),(5,3,'2014-03-31 19:46:46',5),(6,2,'2014-03-31 19:46:46',6),(7,3,'2014-03-31 19:46:46',7),(8,2,'2014-03-31 19:46:46',8),(9,3,'2014-03-31 19:46:46',9),(10,2,'2014-03-31 19:46:46',10),(11,3,'2014-03-31 19:46:46',11),(12,2,'2014-03-31 19:46:46',12),(13,3,'2014-03-31 19:46:46',13),(14,2,'2014-03-31 19:46:46',14),(15,3,'2014-03-31 19:46:46',15),(16,2,'2014-03-31 19:46:46',16);
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

-- Dump completed on 2014-03-31 19:48:00
