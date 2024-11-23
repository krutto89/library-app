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
     