from django.urls import path
from .consumers import GraphConsumer

ws_urlpatterns=[
    path('ws/manager/',GraphConsumer.as_asgi())
]