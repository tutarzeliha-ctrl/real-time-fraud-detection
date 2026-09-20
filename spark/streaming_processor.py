import os
import sys

# Configure Java environment variable and PATH for Docker Linux environment
os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-17-openjdk-amd64"
os.environ['PATH'] = "/usr/lib/jvm/java-17-openjdk-amd64/bin:" + os.environ.get('PATH', '')

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

def create_spark_session():
    print("Initializing Spark Session for Real-Time Fraud Detection & Persistence...")
    
    # Create SparkSession with PostgreSQL JDBC driver and Kafka support for Docker network
    spark = SparkSession.builder \
        .appName("RealTimeFraudDetectionProcessor") \
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.postgresql:postgresql:42.6.0") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.ui.enabled", "false") \
        .getOrCreate()
        
    spark.sparkContext.setLogLevel("WARN")
    return spark

def process_stream():
    spark = create_spark_session()
    
    # Define schema for incoming transaction data from Kafka
    schema = StructType() \
        .add("transaction_id", StringType()) \
        .add("user_id", StringType()) \
        .add("amount", DoubleType()) \
        .add("location", StringType()) \
        .add("timestamp", TimestampType())

    # Read real-time data stream from Kafka topic 'transactions' using Docker internal network
    kafka_stream = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "kafka:9092") \
        .option("subscribe", "transactions") \
        .option("startingOffsets", "latest") \
        .load()

    # Parse JSON values from Kafka messages using the defined schema
    parsed_stream = kafka_stream.selectExpr("CAST(value AS STRING)") \
        .select(from_json(col("value"), schema).alias("data")) \
        .select("data.*")

    # Define the function to write micro-batches directly to PostgreSQL database via Docker service name
    def write_to_postgres(batch_df, batch_id):
        batch_df.write \
            .format("jdbc") \
            .option("url", "jdbc:postgresql://postgres:5432/fraud_db") \
            .option("dbtable", "fraud_transactions") \
            .option("user", "postgres") \
            .option("password", "postgres") \
            .option("driver", "org.postgresql.Driver") \
            .mode("append") \
            .save()
        print(f"Batch {batch_id} successfully written to PostgreSQL.")

    # Write the streaming data using foreachBatch sink
    query = parsed_stream.writeStream \
        .foreachBatch(write_to_postgres) \
        .outputMode("append") \
        .start()

    query.awaitTermination()

if __name__ == "__main__":
    process_stream()