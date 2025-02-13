-- Create the 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
 
-- Insert 10 fake rows into the 'users' table
INSERT INTO users (first_name, last_name, email)
VALUES
    ('John', 'Doe', 'John.Doe@example.com'),
    ('Jane', 'Smith', 'JANE.smith@SPACEX.com'),
    ('Alice', 'Johnson', 'alice.Johnson@example.COM'),
    ('Bob', 'Brown', 'BOB.brown@example.com'),
    ('Charlie', 'Davis', 'CHARLIE.DAVIS@example.com'),
    ('Dana', 'Miller', 'dana.Miller@example.com'),
    ('Eve', 'Wilson', 'EVE.wilson@example.com'),
    ('Frank', 'Taylor', 'frank.taylor@SPACE.com'),
    ('Grace', 'Moore', 'Grace.Moore@example.com'),
    ('Hank', 'Anderson', 'Hank.anderson@example.com');