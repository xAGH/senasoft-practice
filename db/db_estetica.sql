CREATE SCHEMA db_senasoft;
USE db_senasoft;

CREATE TABLE employees(
	uid INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	lastName VARCHAR(50) DEFAULT '',
    service CHAR(4)
);

CREATE TABLE schedules(
	code CHAR(1) PRIMARY KEY NOT NULL,
    timeStart TIME NOT NULL,
    timeEnd	 TIME NOT NULL,
    status CHAR(1)
);

CREATE TABLE services(
	uid CHAR(4) PRIMARY KEY NOT NULL,
    name VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL
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
    service CHAR(4) NOT NULL,
    user INT NOT NULL,
    schedule CHAR(1) NOT NULL
);

CREATE TABLE epmployee_schedule(
	employee INT NOT NULL,
    schedule CHAR(1) NOT NULL
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

INSERT INTO schedules 
VALUES("D", "08:00:00", "11:00:00", "1"),
      ("T", "14:00:00", "17:00:00", "1"),
      ("N", "17:00:00", "20:00:00", "1");
