CREATE DATABASE IF NOT EXISTS cocornell DEFAULT CHARSET=utf8;
USE cocornell;


CREATE TABLE IF NOT EXISTS `user` (
  `netid` varchar(10) PRIMARY KEY,
  `name` varchar(50) NOT NULL,
  `password` varchar (250) NOT NULL,
  `reg_time` datetime NOT NULL DEFAULT NOW()
) DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `board` (
  `id` int(4) AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `list` (
 `id` int(4) AUTO_INCREMENT,
 `board_id` int(4) NOT NULL,
 `name` VARCHAR(50) NOT NULL,
 PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `card` (
  `id` int(4) AUTO_INCREMENT,
  `list_id` int(4) NOT NULL,
  `content` text NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `access` (
  `id` int(8) AUTO_INCREMENT,
  `board_id` int(4) NOT NULL,
  `netid` VARCHAR (10) NOT NULL,
  PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8;
