CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    roll_no VARCHAR(20),
    gender VARCHAR(10),
    contact VARCHAR(15),
    dob VARCHAR(20),
    address TEXT
);
