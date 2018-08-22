from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('threads/<int:subject>/', views.threads, name='threads'),
    path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
]
