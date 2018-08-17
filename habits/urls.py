from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('habits/', views.habits, name='habits'),
    path('habits/new', views.habit_new, name='habit_new'),
    path('habits/<int:habit_id>/edit', views.habit_edit, name='habit_edit'),
    path('habits/<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('delete/<int:pk>/', views.HabitDelete.as_view(), name='habit_delete'),

    path('habits/<int:habit_id>/new_action', views.action_new, name='action_new'),
    path('habits/<int:habit_id>/<int:pk>/edit_action', views.action_edit, name='action_edit'),
    path('delete_action/<int:pk>/', views.ActionDelete.as_view(), name='action_delete'),

    path('habits/motives', views.motives, name='motives'),
    path('habits/new_motive', views.motive_new, name='motive_new'),
    path('habits/<int:pk>/edit_motive', views.motive_edit, name='motive_edit'),

    path('', views.reconneqt, name='reconneqt'),
]
