CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO users (name) VALUES
('Mirza'),
('DevOps Student'),
('Linux Admin');