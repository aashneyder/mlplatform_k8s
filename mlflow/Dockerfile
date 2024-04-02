# Defining base image
FROM python:3.9.2-slim
# Installing MLflow from PyPi
RUN pip install mlflow boto3
EXPOSE 5000
ENTRYPOINT ["mlflow", "server", "--host", "0.0.0.0"]
