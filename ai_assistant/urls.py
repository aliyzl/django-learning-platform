from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='ai_chat'),
    path('context/<int:lesson_id>/', views.get_lesson_context_api, name='ai_lesson_context'),
]




