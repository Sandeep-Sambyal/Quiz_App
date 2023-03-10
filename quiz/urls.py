"""Urls of quiz app"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<pk>/', views.quiz_page, name='quiz_page'),
    path('<pk>/save_quiz/', views.save_quiz, name='save_quiz')
]