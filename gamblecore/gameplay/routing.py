from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/play/$", consumers.GameplayConsumer.as_asgi()),
]