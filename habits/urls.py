from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

    path('habits/new/', views.habit_new, name='habit_new'),
    path('habits/<int:habit_id>/edit/', views.habit_edit, name='habit_edit'),
    path('habits/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('delete/<int:pk>/', views.HabitDelete.as_view(), name='habit_delete'),

    path('habits/<int:habit_id>/new_action/', views.action_new, name='action_new'),
    path('habits/<int:habit_id>/<int:pk>/edit_action/', views.action_edit, name='action_edit'),
    path('delete_action/<int:pk>/', views.ActionDelete.as_view(), name='action_delete'),

    path('motives/', views.motives, name='motives'),
    path('motives/new/', views.motive_new, name='motive_new'),
    path('motives/<int:pk>/edit/', views.motive_edit, name='motive_edit'),
    path('delete_motive/<int:pk>/', views.MotiveDelete.as_view(), name='motive_delete'),

    path('progress/', views.progress, name='progress'),
    path('forum/', views.forum, name='forum'),
]

handler404 = views.error_404
handler500 = views.error_500
