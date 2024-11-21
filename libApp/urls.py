from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/<str:username>/', views.profile, name='profile'),
    # path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
]