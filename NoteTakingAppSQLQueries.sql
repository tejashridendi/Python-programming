--created a database named 'notespro' for the note taking desktop application
create database notespro;
--created a table 'notes' in database named 'notespro' for the note taking desktop application with columns - ID for note id, text for note text and status column for marking as completed/pending
create table notespro.notes(
id INT AUTO_INCREMENT NOT NULL UNIQUE, text VARCHAR(255) NOT NULL,status ENUM('pending', 'completed') DEFAULT 'pending'
);