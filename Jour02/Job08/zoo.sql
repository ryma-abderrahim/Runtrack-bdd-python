/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS animal;
CREATE TABLE `animal` (
  `id` int NOT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `race` varchar(25) DEFAULT NULL,
  `cage_id` int DEFAULT NULL,
  `date_naissance` date DEFAULT NULL,
  `pays_origine` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

DROP TABLE IF EXISTS cage;
CREATE TABLE `cage` (
  `id` int NOT NULL,
  `superficie` int DEFAULT NULL,
  `capacité_max` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
