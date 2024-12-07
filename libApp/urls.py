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
    path('editmembers/<int:id>/',views.membersEdit, name='editmembers'),
    path('deletemembers/<int:id>/',views.membersDelete, name='deletemembers'),
    path ('updatemembers/<int:id>/',views.updateMembers, name='updatemembers'),
    path('editborrowers/<int:id>/',views.borrowersEdit, name='editborrower'),
    path('deleteborrowers/<int:id>/',views.deleteBorrowers, name='deleteborrower'),
    path ('updateborrowers/<int:id>/',views.updateBorrowers, name='updateborrower'),
    path('sld/',views.studentLib, name='studentlibdashboard'),
    path('studentbooks/',views.studentBooks, name='studentbooks'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow_book'),
    path('borrowconfim/',views.borrow_confirmation , name='borrow_confirmation'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('help/',views.tips, name='tips'),
    path('logout/', views.logout_view, name='logout'),

    
    # path('librarian-login/', views.librarian_login, name='librarian_login'),
    # path('search/', views.search_books, name='search_books'),
    # path('logout/', views.logout_view, name='logout'),
    # path('profile/<str:username>/', views.profile, name='profile'),
    # path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),
    # path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
]