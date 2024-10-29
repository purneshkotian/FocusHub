from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from.consumers import TaskConsumer

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls))
]

websocket_urlpatterns = [
    path('ws/tasks/', TaskConsumer.as_asgi()),
]