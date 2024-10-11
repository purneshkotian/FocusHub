from celery import shared_task

@shared_task
def send_task_notification(task_id):
    print(f"Notification sent for task with ID: {task_id}")
