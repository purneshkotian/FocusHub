from celery import shared_task
from kafka import KafkaConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from .models
import json

@shared_task
def notification_consumer():
    consumer = KafkaConsumer(
        'task_notifications',
        bootstrap_servers='kafka:9092',
        group_id='task_notifications_group'
    )
    channel_layer = get_channel_layer()

    for message in consumer:
        # Decode the message value from bytes to string
        message_value = message.value.decode('utf-8')

        # Send the JSON-decoded message to WebSocket
        async_to_sync(channel_layer.group_send)(
            'tasks',
            {
                'type': 'send_task_update',
                'message': json.loads(message_value)  # Ensure it's a dictionary or JSON serializable object
            }
        )