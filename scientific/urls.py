from django.urls import path
from . import views

urlpatterns = [
    path('', views.sci_posts, name='sci_posts'),
]