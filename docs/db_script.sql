-- MySQL Script generated by MySQL Workbench
-- Wed Mar 19 14:24:09 2025
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_crud_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_crud_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_crud_schema` DEFAULT CHARACTER SET utf8 ;
USE `db_crud_schema` ;

-- -----------------------------------------------------
-- Table `db_crud_schema`.`administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`administrador` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(18) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefone_UNIQUE` (`telefone` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_crud_schema`.`aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`aluno` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(18) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_crud_schema`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`cursos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `descricao` TEXT NOT NULL,
  `carga_horaria` INT NOT NULL,
  `instrutor` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_crud_schema`.`inscricoes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_crud_schema`.`inscricoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cursos_id` INT NOT NULL,
  `aluno_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_inscricoes_aluno1_idx` (`aluno_id` ASC) VISIBLE,
  INDEX `fk_inscricoes_cursos_idx` (`cursos_id` ASC) VISIBLE,
  CONSTRAINT `fk_inscricoes_cursos`
    FOREIGN KEY (`cursos_id`)
    REFERENCES `db_crud_schema`.`cursos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_inscricoes_aluno1`
    FOREIGN KEY (`aluno_id`)
    REFERENCES `db_crud_schema`.`aluno` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
