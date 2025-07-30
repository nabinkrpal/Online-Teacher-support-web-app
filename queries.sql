show databases;
create database teacher_connect;
drop database ;
use teacher_connect;
show tables;

select * from login;
select * from teacher;
select * from student;
select * from feedback; 
update feedback
set message="Nice"
where message="bhangbhosda";

-- login table
CREATE TABLE login (
    usernm VARCHAR(50) PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL
);

-- teacher table
CREATE TABLE teacher (
    usernm VARCHAR(50) PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100),
    no VARCHAR(20),
    dob DATE,
    gender VARCHAR(10),
    about TEXT,
    adharno VARCHAR(20),
    topics TEXT,
    pimg VARCHAR(255),
    qimg VARCHAR(255)
);

-- student table
CREATE TABLE student (
    usernm VARCHAR(50) PRIMARY KEY,
    passwd VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100),
    no VARCHAR(20),
    dob DATE,
    gender VARCHAR(10),
    adharno VARCHAR(20),
    pimg VARCHAR(255)
);

-- feedback table
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    source VARCHAR(100) NOT NULL,
    message TEXT NOT NULL
);
