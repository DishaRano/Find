from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.video, name='video'),
    path('', views.home),
]