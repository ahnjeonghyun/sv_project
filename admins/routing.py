from django.urls import path, re_path

from .           import consumers


websocket_urlpatterns = [
    path('admin',consumers.Admin.as_asgi()),
]