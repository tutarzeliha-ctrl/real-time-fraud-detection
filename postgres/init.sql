CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50),
    amount DOUBLE PRECISION,
    timestamp TIMESTAMP,
    location VARCHAR(100),
    is_fraud BOOLEAN
);