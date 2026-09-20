import os
import pyspark

# Configure environment paths for Windows and Java 17
os.environ['SPARK_HOME'] = os.path.dirname(pyspark.__file__)
os.environ['JAVA_HOME'] = r'C:\Java\OpenJDK17U-jdk_x64_windows_hotspot_17.0.12_7\jdk-17.0.12+7'
os.environ['PATH'] = os.path.join(os.environ['JAVA_HOME'], 'bin') + ';' + os.environ['PATH']

from pyspark.sql import SparkSession

print("Starting Spark session test with Java 17 options...")
spark = SparkSession.builder \
    .appName("TestSession") \
    .config("spark.driver.memory", "1g") \
    .config("spark.driver.extraJavaOptions", "--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.invoke=ALL-UNNAMED --add-opens=java.base/java.util=ALL-UNNAMED") \
    .getOrCreate()

print("Spark session successfully created!")
print(spark)
spark.stop()