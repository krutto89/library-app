from django.contrib import admin
from .models import CustomUser ,Book , Members
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Book)

admin.site.register(Members)



