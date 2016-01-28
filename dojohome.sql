-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema dojobyte
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dojobyte
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dojobyte` DEFAULT CHARACTER SET utf8 ;
USE `dojobyte` ;

-- -----------------------------------------------------
-- Table `dojobyte`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojobyte`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `alias` VARCHAR(50) NULL DEFAULT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `location` VARCHAR(255) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dojobyte`.`restaurants`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojobyte`.`restaurants` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `restaurant_name` VARCHAR(255) NULL DEFAULT NULL,
  `genre` VARCHAR(255) NULL,
  `liked` INT(11) NULL DEFAULT NULL,
  `hated` INT(11) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dojobyte`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojobyte`.`favorites` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `restaurant_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_have_favorites_users1_idx` (`user_id` ASC),
  INDEX `fk_users_have_favorites_restaurants1_idx` (`restaurant_id` ASC),
  CONSTRAINT `fk_users_have_favorites_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `dojobyte`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_have_favorites_restaurants1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `dojobyte`.`restaurants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `dojobyte`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dojobyte`.`reviews` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `review_text` VARCHAR(255) NULL DEFAULT NULL,
  `helpful` INT(11) NULL DEFAULT NULL,
  `unhelpful` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NOT NULL,
  `restaurant_id` INT(11) NOT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reviews_users_idx` (`user_id` ASC),
  INDEX `fk_reviews_restaurants1_idx` (`restaurant_id` ASC),
  CONSTRAINT `fk_reviews_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `dojobyte`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_restaurants1`
    FOREIGN KEY (`restaurant_id`)
    REFERENCES `dojobyte`.`restaurants` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
