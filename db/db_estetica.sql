CREATE SCHEMA db_estetica;
USE db_estetica;

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

CREATE TABLE customers(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(125) NOT NULL,
    password VARCHAR(30) NOT NULL
);

CREATE TABLE appointments(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    employee INT NOT NULL,
    service TINYINT NOT NULL,
    customer INT NOT NULL,
    schedule INT NOT NULL
);

CREATE TABLE epmployee_schedule(
	employee INT NOT NULL,
    schedule INT NOT NULL
);

CREATE TABLE favorites(
	employee INT NOT NULL,
    customer INT NOT NULL
);

ALTER TABLE employees
	ADD FOREIGN KEY (service) REFERENCES services(uid);
    
ALTER TABLE appointments 
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (service) REFERENCES services(uid),
    ADD FOREIGN KEY (customer) REFERENCES customers(uid),
    ADD FOREIGN KEY (schedule) REFERENCES schedules(code)
;

ALTER TABLE epmployee_schedule
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (schedule) REFERENCES schedules(code)
;

ALTER TABLE favorites
	ADD FOREIGN KEY (employee) REFERENCES employees(uid),
    ADD FOREIGN KEY (customer) REFERENCES customers(uid)
;


