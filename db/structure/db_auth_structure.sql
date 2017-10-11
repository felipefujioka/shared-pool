CREATE TABLE users (
    id INTEGER SERIAL PRIMARY KEY,
    email TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT current_timestamp,
    updated_at TIMESTAMP DEFAULT current_timestamp
);

CREATE TABLE password_credentials (
    user_id INTEGER REFERENCES users(id) PRIMARY KEY,
    password_hash TEXT NOT NULL,
    updated_at TIMESTAMP DEFAULT current_timestamp
);

