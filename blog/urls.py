from django.urls import path
from . import views #import from views.py file and retrieves any function within it;.

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]