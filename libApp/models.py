from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # add any additional custom fields here    
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
    # image = models.ImageField(upload_to='images/')
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title