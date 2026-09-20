CREATE TABLE IF NOT EXISTS transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    merchant VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_fraud BOOLEAN DEFAULT FALSE
);

-- Set Replica Identity to FULL for Debezium CDC
ALTER TABLE transactions REPLICA IDENTITY FULL;

-- Insert sample data for testing
INSERT INTO transactions (user_id, amount, merchant, location, is_fraud) 
VALUES 
(101, 250.00, 'TechStore', 'New York', FALSE),
(102, 4500.50, 'LuxuryWatch', 'Dubai', TRUE),
(103, 45.20, 'GroceryMarket', 'London', FALSE);