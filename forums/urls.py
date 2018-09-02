from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('subject/<int:s_id>/', views.threads, name='threads'),
    path('thread/new/', views.thread_create, name='thread_new'),
    path('thread/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('thread/delete/<int:pk>', views.ThreadDelete.as_view(), name='thread_delete'),
    path('thread/edit/<int:pk>', views.thread_edit, name='thread_edit'),
    path('post/reply/<int:pk>/', views.post_create, name='post_new'),
    path('post/delete/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
]
