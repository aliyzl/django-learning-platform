from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('<slug:course_slug>/<slug:section_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
    path('api/lesson/<int:lesson_id>/content/', views.api_lesson_content, name='api_lesson_content'),
    path('api/lesson/<int:lesson_id>/progress/', views.update_progress, name='update_progress'),
]




