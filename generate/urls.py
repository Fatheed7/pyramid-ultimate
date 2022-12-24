from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='generate'),
    path('create/', views.create_run, name='create'),
]
