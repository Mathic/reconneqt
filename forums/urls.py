from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('thread/<int:pk>/', views.forum_thread, name='forum_subject'),
]
