-- MySQL Script generated by MySQL Workbench
-- Thu Jun 28 17:11:58 2018
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema throughmypain
-- -----------------------------------------------------
DROP DATABASE IF EXISTS `throughmypain` ;

-- -----------------------------------------------------
-- Schema throughmypain
-- -----------------------------------------------------
CREATE DATABASE IF NOT EXISTS `throughmypain` DEFAULT CHARACTER SET utf8;
USE `throughmypain` ;

-- -----------------------------------------------------
-- Table `throughmypain`.`Users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Users` (
  `User_ID` VARCHAR(50) NOT NULL,
  `user_passwd` VARCHAR(50) NOT NULL,
  `user_name` VARCHAR(50) NOT NULL,
  `age` INT NOT NULL,
  `gender` VARCHAR(50) NOT NULL,
  `records_number` INT NOT NULL,
  `last_record_date` VARCHAR(50) NOT NULL,
  `create_at` VARCHAR(50) NOT NULL,
  `admin` BOOLEAN NOT NULL,
  PRIMARY KEY (`User_ID`),
  UNIQUE INDEX `index_user_name` (`user_name` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `throughmypain`.`Records`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Records` (
  `Record_ID` VARCHAR(50) NOT NULL,
  `create_at` VARCHAR(50) NOT NULL,
  `pain_number` INT NOT NULL,
  `record_brief` VARCHAR(50) NOT NULL,
  `User_ID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Record_ID`),
  INDEX `User_ID_idx` (`User_ID` ASC),
  CONSTRAINT `User_ID`
    FOREIGN KEY (`User_ID`)
    REFERENCES `throughmypain`.`Users` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `throughmypain`.`Pains`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Pains` (
  `Pain_ID` VARCHAR(50) NOT NULL,
  `region_count` INT NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `pain_character` VARCHAR(50) NOT NULL,
  `pain_severity` INT NOT NULL,
  `depth` VARCHAR(50) NOT NULL,
  `frequency` VARCHAR(50) NOT NULL,
  `Record_ID` VARCHAR(50) NOT NULL,
  `Users_User_ID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Pain_ID`),
  INDEX `Record_ID_idx` (`Record_ID` ASC),
  INDEX `fk_Pains_Users1_idx` (`Users_User_ID` ASC),
  CONSTRAINT `Record_ID`
    FOREIGN KEY (`Record_ID`)
    REFERENCES `throughmypain`.`Records` (`Record_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Pains_Users1`
    FOREIGN KEY (`Users_User_ID`)
    REFERENCES `throughmypain`.`Users` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `throughmypain`.`Regions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Regions` (
  `Region_ID` VARCHAR(50) NOT NULL,
  `region_severity` INT NOT NULL,
  `cells_count` INT NOT NULL,
  `Pain_ID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Region_ID`),
  INDEX `Pain_ID_idx` (`Pain_ID` ASC),
  CONSTRAINT `Pain_ID`
    FOREIGN KEY (`Pain_ID`)
    REFERENCES `throughmypain`.`Pains` (`Pain_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `throughmypain`.`Cells`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Cells` (
  `Cell_ID` VARCHAR(50) NOT NULL,
  `cell_severity` INT NOT NULL,
  `Region_ID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Cell_ID`),
  INDEX `Region_ID_idx` (`Region_ID` ASC),
  CONSTRAINT `Region_ID`
    FOREIGN KEY (`Region_ID`)
    REFERENCES `throughmypain`.`Regions` (`Region_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `throughmypain`.`Reports`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `throughmypain`.`Reports` (
  `Report_ID` VARCHAR(50) NOT NULL,
  `chart_number` INT NOT NULL,
  `create_at` VARCHAR(50) NOT NULL,
  `User_ID` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`Report_ID`),
  INDEX `User_ID_idx` (`User_ID` ASC),
  CONSTRAINT `user`
    FOREIGN KEY (`User_ID`)
    REFERENCES `throughmypain`.`Users` (`User_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

drop user 'ubuntu'@'localhost';
flush privileges;
CREATE USER 'ubuntu'@'localhost' identified by 'ubuntu';
GRANT SELECT, ALTER, DROP, INSERT, UPDATE, DELETE ON TABLE `throughmypain`.* TO 'ubuntu'@'localhost';

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
