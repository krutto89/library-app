from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/',views.books_view, name='books'),
    path('addbooks/', views.books_add, name='addbooks'),
    path('members/', views.members, name='members'),
    path('addmembers/', views.members_add, name='addmembers'),
    path('borrowers/', views.borrowers, name='borrowers'),
    path('addborrowers/', views.borrowers_add, name='addborrowers'),
    path('editbooks/<int:id>/',views.bookEdit, name='editbooks'),
    path('deletebooks/<int:id>/',views.bookDelete, name='deletebooks'),
    path ('updatebooks/<int:id>/',views.updateBooks, name='updatebooks'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/<str:username>/', views.profile, name='profile'),
    # path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
]