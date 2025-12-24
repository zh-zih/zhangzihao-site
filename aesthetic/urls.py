from django.urls import path
from . import views

urlpatterns = [
    path('', views.aes_posts, name='aes_posts'),
]