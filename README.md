# Real-Time Fraud Detection Pipeline

An end-to-end real-time data engineering and streaming analytics pipeline designed to detect fraudulent financial transactions instantly. This project leverages modern distributed data tools and microservices architecture deployed via Docker.

## 🚀 Architecture & Tech Stack

* **Stream Processing & Message Broker:** Apache Kafka (KRaft mode) for ingestion and event streaming.
* **Real-Time Data Processing:** PySpark Structured Streaming for stateful aggregations and rule-based anomaly detection.
* **Storage & Persistence:** PostgreSQL for relational data storage and historical persistence.
* **Monitoring & Visualization:** Streamlit interactive dashboard providing live metrics, transaction logs, and anomaly tracking.
* **Containerization:** Docker & Docker Compose for seamless multi-service orchestration.

## 📂 Project Structure

```text
real-time-fraud-detection/
│
├── spark/
│   └── streaming_processor.py   # PySpark streaming consumer & logic
├── Dockerfile                   # Custom image configuration for Spark processor
├── docker-compose.yml           # Multi-container orchestration setup
├── producer.py                  # Real-time transaction event generator
├── app.py                       # Streamlit monitoring dashboard
└── requirements.txt             # Python dependencies
⚙️ Getting Started & Installation
Prerequisites
Docker and Docker Compose installed on your machine.

Python 3.10+ (for running local producers and dashboards).

1. Clone the Repository
Bash
git clone [https://github.com/your-username/real-time-fraud-detection.git](https://github.com/your-username/real-time-fraud-detection.git)
cd real-time-fraud-detection
2. Run the Infrastructure
Build and spin up the microservices (Kafka, PostgreSQL, and Spark Processor) using Docker Compose:

Bash
docker compose up --build -d
3. Run the Data Producer
Start producing mock streaming transactions into the Kafka topic:

Bash
python producer.py
4. Launch the Streamlit Dashboard
Open a separate terminal window and start the monitoring interface:

Bash
streamlit run app.py
Access the dashboard in your browser at http://localhost:8501.

📊 Dashboard Features
Live Metrics: Real-time throughput counters for total transactions and flagged fraud cases.

Dynamic Table: Auto-refreshing grid displaying recent transaction streams with location and amount details.