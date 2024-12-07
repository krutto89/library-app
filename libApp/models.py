from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # add any additional custom fields here    
    #role field to differentiate between librarians and students
    ROLE_CHOICES =[
        ('Librarian', 'Librarian'),
        ('Student', 'Student'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['username','password'],
                name = 'unique_username_password'
            )
        ]
    def __str__(self):
        return self.username
     
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     publication_date = models.DateField()
#     isbn = models.CharField(max_length=13)
#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['title','author','publication_date','isbn'],
#                 name = 'unique_book'
#             )
#         ]

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', null= True, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Members(models.Model):
    names = models.CharField(max_length=100)
    regNo = models.CharField(max_length=100)
    levels = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    dateJoined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class BorrowersList(models.Model):
    names = models.CharField(max_length=100)
    regNo = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
    dateJoined = models.DateTimeField(auto_now_add=True)
    # bkBorrowed = models.ForeignKey(Book, on_delete=models.CASCADE)
    levels = models.CharField(max_length=100)
    bkBorrowed = models.CharField(max_length=100)
    dueDate = models.DateTimeField()

    def __str__(self):
        return self.name
    

class BorrowedBook(models.Model):
    user = models.ForeignKey(Members, on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)      
    borrow_date = models.DateTimeField(auto_now_add=True)      
    return_date = models.DateTimeField(null=True, blank=True)     
    liked = models.BooleanField(default=False)                    # If user liked the book

    def __str__(self):
        return f"{self.user.names} borrowed {self.book.title}"
