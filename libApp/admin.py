from django.contrib import admin
from .models import CustomUser ,Book , Members,BorrowersList
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Book)
admin.site.register(BorrowersList)
admin.site.register(Members)



