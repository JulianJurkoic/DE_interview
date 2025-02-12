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
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Bob', 'Brown', 'bob.brown@example.com'),
    ('Charlie', 'Davis', 'charlie.davis@example.com'),
    ('Dana', 'Miller', 'dana.miller@example.com'),
    ('Eve', 'Wilson', 'eve.wilson@example.com'),
    ('Frank', 'Taylor', 'frank.taylor@example.com'),
    ('Grace', 'Moore', 'grace.moore@example.com'),
    ('Hank', 'Anderson', 'hank.anderson@example.com');