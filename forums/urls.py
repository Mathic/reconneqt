from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('subject/<int:s_id>/', views.threads, name='threads'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
]
