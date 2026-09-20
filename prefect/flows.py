from prefect import flow, task
import subprocess

@task
def docker_start():
    subprocess.run(["docker-compose", "up", "-d"])

@task
def run_producer():
    subprocess.Popen(["python", "producer.py"])

@flow
def fraud_pipeline_flow():
    docker_start()
    run_producer()

if __name__ == "__main__":
    fraud_pipeline_flow()