 # Student Management System

A user-friendly *Student Management System* built with *Python, **MySQL, and **Tkinter* that supports adding, viewing, updating, deleting, and searching student records. This project aims to provide a simple yet effective interface for managing student information in a relational database.

## Features

- *Add New Students*: Easily insert new student records (Name, Roll No, Gender, Contact, DOB, Address).
- *View Records*: Display all existing records in a tabular form using a Treeview.
- *Update & Delete*: Modify or remove existing records with a single click.
- *Search: Filter records by **Name* or *Roll No* to quickly locate a student.
- *Intuitive GUI: Built with **Tkinter* for a clean and user-friendly interface.
- *Real-Time Data…
 # Student Management System

A *user-friendly* Student Management System built with *Python, **MySQL, and **Tkinter*. This application supports adding, viewing, updating, deleting, and searching student records, providing an intuitive interface for managing student information.

## Features

- *Add New Students*: Insert new student records with details like Name, Roll No, Gender, Contact, DOB, and Address.
- *View Records*: Display all student records in a table (Treeview).
- *Update & Delete*: Modify or remove any existing student record with a single click.
- *Search: Quickly find records by **Name* or *Roll No*.
- *Clean GUI: Built with **Tkinter*, offering a straightforward and user-friendly interface.
- *Robust Data Storage: Utilizes **MySQL* for secure, reliable data management.

## Prerequisites

- *Python* 3.x installed.
- *MySQL* Server installed and running.
- A MySQL user account (for example, root) with a known password.
- *mysql-connector-python* library (install via pip install mysql-connector-python).

## Getting Started

1. *Clone or Download the Repository*  
   - Clone:  
     bash
     git clone https://github.com/<YourUsername>/StudentManagementSystem.git
       
   - Or download the ZIP and extract it.

2. *Create the Database*  
   - Open MySQL Workbench (or any client) and run:
     sql
     CREATE DATABASE student_db;
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
     
   - Adjust table structure as needed.

3. *Update main.py*  
   - Open main.py and modify the following lines with your MySQL credentials and database name:
     python
     conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="Siddhi@123",
         database="student_db"
     )
     

4. *Install Dependencies*  
   - In your project folder, install MySQL Connector:
     bash
     pip install mysql-connector-python
     

5. *Run the Application*  
   ```bash
   python main.py


   ![Uploading screenshot1.jpeg…]()


   
