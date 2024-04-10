CREATE DATABASE library_management;

USE library_management;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    genre VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    publication_date DATE,
    availability BOOLEAN DEFAULT 1,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE authors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    library_id VARCHAR(10) NOT NULL UNIQUE
);

CREATE TABLE borrowed_books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
	user VARCHAR(100) NOT NULL,
    borrow_date DATE NOT NULL,
    return_date DATE,
	book_id INT,
	user_id INT,
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


SET SQL_SAFE_UPDATES = 0;
DELETE FROM books
WHERE id;
SET SQL_SAFE_UPDATES = 1;

SELECT *
FROM books;

SET SQL_SAFE_UPDATES = 0;
DELETE FROM borrowed_books
WHERE id;
SET SQL_SAFE_UPDATES = 1;

SELECT *
FROM borrowed_books;

SELECT *
FROM users;

SELECT *
FROM authors;