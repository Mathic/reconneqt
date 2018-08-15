from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('habits/', views.habits, name='habits'),
    path('habits/<int:habit_id>/', views.detail, name='detail'),
    path('', views.reconneqt, name='reconneqt'),
]
