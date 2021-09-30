CREATE SCHEMA db_senasoft;
USE db_senasoft;

CREATE TABLE employees(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) DEFAULT '',
    service TINYINT
);

CREATE TABLE schedules(
	code INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    timeStart TIME NOT NULL,
    timeEnd	 TIME NOT NULL,
    status CHAR(1)
);

CREATE TABLE services(
	uid TINYINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    price INT NOT NULL
);

CREATE TABLE users(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(125) NOT NULL,
    password VARCHAR(400) NOT NULL,
    is_admin CHAR(1) NOT NULL DEFAULT '0'
);

CREATE TABLE appointments(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    employee INT NOT NULL,
    service TINYINT NOT NULL,
    user INT NOT NULL,
    schedule INT NOT NULL
);

CREATE TABLE epmployee_schedule(
	employee INT NOT NULL,
    schedule INT NOT NULL
);

CREATE TABLE favorites(
	employee INT NOT NULL,
    user INT NOT NULL
);

ALTER TABLE employees
	ADD FOREIGN KEY (service) REFERENCES services(uid);
    
ALTER TABLE appointments 
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (service) REFERENCES services(uid),
    ADD FOREIGN KEY (user) REFERENCES users(uid),
    ADD FOREIGN KEY (schedule) REFERENCES schedules(code)
;

ALTER TABLE epmployee_schedule
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (schedule) REFERENCES schedules(code)
;

ALTER TABLE favorites
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (user) REFERENCES users(uid)
;


