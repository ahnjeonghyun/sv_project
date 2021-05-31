from django.urls import path, re_path

from .           import consumers


websocket_urlpatterns = [
    path('quizes', consumers.QuizLoad.as_asgi())
]