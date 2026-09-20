import json
import time
import random
from datetime import datetime
from confluent_kafka import Producer

def generate_transaction():
    return {
        "transaction_id": f"txn_{random.randint(10000, 99999)}",
        "user_id": f"user_{random.randint(100, 500)}",
        "amount": round(random.uniform(10.0, 15000.0), 2),
        "location": random.choice(["New York", "London", "Istanbul", "Berlin", "Tokyo"]),
        "timestamp": datetime.now().isoformat()
    }

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}]")

def run_producer():
    print("Starting Confluent Kafka Transaction Producer...")
    
    conf = {
        'bootstrap.servers': '127.0.0.1:9092',
        'broker.address.family': 'v4'
    }
    producer = Producer(conf)
    topic_name = "transactions"
    
    print(f"Connected to Kafka successfully. Producing messages to topic '{topic_name}'...")

    try:
        while True:
            transaction = generate_transaction()
            producer.produce(
                topic_name,
                key=transaction["transaction_id"],
                value=json.dumps(transaction),
                callback=delivery_report
            )
            producer.poll(0)
            print(f"Produced transaction: {transaction}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Producer stopped by user.")
    finally:
        producer.flush()

if __name__ == "__main__":
    run_producer()