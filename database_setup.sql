mysql -u root -p /*Log in to MySQL as a user with administrative privileges. You'll need to provide the MySQL root password when prompted.*/
CREATE DATABASE library_db;
-- Create the books table
CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    published_year YEAR,
    availability BOOLEAN DEFAULT TRUE
);
