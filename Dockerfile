FROM eclipse-temurin:17-jdk-jammy
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH="$JAVA_HOME/bin:$PATH"
SHELL ["/bin/bash", "-c"]

# Set Java environment variables
ENV JAVA_HOME=/opt/java/openjdk
ENV PATH="$JAVA_HOME/bin:$PATH"

# Install Python, pip, and curl
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/lib/jvm && ln -s /opt/java/openjdk /usr/lib/jvm/java-17-openjdk-amd64

# Set working directory inside container
WORKDIR /app

# Copy requirements and install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=1000 -r requirements.txt

# Copy the rest of the project files
COPY . .

# Command to run the streaming processor
CMD ["python3", "spark/streaming_processor.py"]
