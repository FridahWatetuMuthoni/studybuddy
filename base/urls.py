from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('logout/', views.logout_page, name='logout'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register, name='register'),

    # user
    path('profile/<str:pk>/', views.user_profile, name='user-profile'),
    path('update-user/', views.user_update, name='update-user'),

    # home and rooms
    path('', views.homepage, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('create/', views.room_create, name='create-room'),
    path('update/<str:pk>/', views.room_update, name='update-room'),
    path('delete/<str:pk>/', views.room_delete, name='delete-room'),
    path('delete/message/<str:pk>/', views.delete_message, name='delete-message'),

    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),

]
