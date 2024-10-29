import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('tasks', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('tasks', self.channel_name)

    async def send_task_update(self, event):
        # Ensure that `event['message']` is a dictionary or JSON serializable object
        await self.send(text_data=json.dumps(event['message']))
