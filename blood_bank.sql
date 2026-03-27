CREATE DATABASE blood_bank;
USE blood_bank;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) UNIQUE NOT NULL, password VARCHAR(100) NOT NULL,role ENUM('staff','hospital') NOT NULL);
CREATE TABLE donors(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,blood_group VARCHAR(5) NOT NULL,phone VARCHAR(15),last_donation_date DATE,next_eligible_date DATE);
CREATE TABLE blood_requests(id INT AUTO_INCREMENT PRIMARY KEY,hospital_name VARCHAR(100),blood_group VARCHAR(5),units_requested INT,status ENUM('Pending','Approved','Fullfilled')DEFAULT 'Pending');

