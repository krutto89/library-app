from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.hashers import check_password
# from django.contrib.auth import authenticate,login as auth_login
# Create your views here.
def login(request):
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

def dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists with the given username
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None

        if user and check_password(password, user.password):
            # If user exists and password is correct, redirect to dashboard
            return render(request, 'dashboard.html', {'user': user})
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to login page

    # If not a POST request, simply show the login page
    return render(request, 'login.html')

    



        