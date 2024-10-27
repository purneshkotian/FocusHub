#!/bin/bash
while ! curl -s kafka:9092; do
  echo "Waiting for Kafka..."
  sleep 5
done
echo "Kafka is up and running."
celery -A task_management worker --loglevel=info

