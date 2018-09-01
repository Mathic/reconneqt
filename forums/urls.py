from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('subject/<int:s_id>/', views.threads, name='threads'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('post/reply/<int:pk>/', views.post_create, name='post_new'),
    path('thread/new/', views.thread_create, name='thread_new'),
]
