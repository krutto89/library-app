from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
# Create your views here.
def login (request):
    return render(request,'login.html')


def register (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password','').strip()
        confirm_password = request.POST.get('confirm_password','').strip()
        
        if not username or not password or not confirm_password:
            return render(request,'register.html',{'error':'All fields are required'})

        if password != confirm_password:
            return render(request,'register.html',{'error':'Password does not match'})
        try:
            user = CustomUser(username=username)
            user.set_password(password)
            user.save()
           
            return redirect('login')
        except IntegrityError:
            return render(request, 'register.html',{
                'error':'Username already exists'
            })
    return render(request,'register.html')

def dashboard (request):
    return render(request,'dashboard.html')