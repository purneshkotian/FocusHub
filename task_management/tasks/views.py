from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from kafka import KafkaProducer
import json

# Initialize the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('assigned_to').all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        # Use the serializer to validate and create a new task from the request data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_task = serializer.save()  # This saves the task to the database
            # Attempt to send the task creation event to Kafka
            try:
                producer.send('task_notifications', {'task_id': new_task.id})
            except Exception as e:
                # Return a 500 response if Kafka fails
                return Response({'error': f'Kafka error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # If Kafka send is successful, return the serialized task data
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return 400 response if serializer validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            # try:
            #     # producer.send('task_notifications', json.dumps({'task_id': new_task.id}).encode('utf-8'))
            #     # Sending task creation event to Kafka topic
            #     producer.send('task_updates', {
            #         'task_id': new_task.id,
            #         'title': new_task.title,
            #         'status': new_task.status,
            #         'event': 'Task Created'
            #     })
            # except Exception as e:
            #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

