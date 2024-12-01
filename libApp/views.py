from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Book ,Members ,BorrowersList
from .forms import BookForm , MemberForm ,BorrowerForm
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

def books_view(request):
    allBooks = Book.objects.all()
    context = {'bks':allBooks}
    return render (request, 'books-page.html', context)
    

def books_add(request):
    if request.method == 'POST':
        books = Book (
            title = request.POST['title'],
            author = request.POST['author'],
            category = request.POST['category'],
            quantity = int(request.POST['quantity']),
            image = request.FILES['image']
        )
        books.save()
        return redirect('/books')
    else:
        return render(request, 'add-books.html')
   
def members(request):
    allMembers = Members.objects.all()
    context = {'mems':allMembers}
    return render (request, 'members.html', context)

def members_add(request):
    if request.method == 'POST':
        memb = Members (
            names = request.POST['names'],
            regNo = request.POST['regNo'],
            levels = request.POST['levels'],
            phoneNumber = request.POST['phoneNumber'],
        )
        memb.save()
        return redirect('/members')
    else:
        return render(request, 'add-members.html')
    
def borrowers(request):
    allBorrowers = BorrowersList.objects.all()
    context = {'brws':allBorrowers}
    return render (request, 'borrowers.html', context)
        

def borrowers_add(request):
    if request.method == 'POST':
        borrow = BorrowersList (
            names = request.POST['names'],
            regNo = request.POST['regNo'],
            phoneNumber = request.POST['phoneNumber'],
            levels = request.POST['levels'],
            bkBorrowed = request.POST['bkBorrowed'],
            dueDate = request.POST['dueDate'],
        )
        borrow.save()
        return redirect('/borrowers')
    else:
        return render(request, 'add-borrowers.html')

def bookEdit(request,id): #rendering the edit form with prefilled data for the selected book
    editbooks = Book.objects.get(id=id)
    return render(request, 'edit-books.html', {'bookss':editbooks})

def updateBooks(request,id): #handles form submission and updates the selected book details in the database
    updatebks = Book.objects.get(id=id)
    form  = BookForm(request.POST,request.FILES , instance= updatebks)

    if form.is_valid():
        form.save()
        return redirect('/books')
    else:
        return render(request, 'edit-books.html', {'bookss':updatebks})


def bookDelete(request,id):
    deletebks = Book.objects.get(id=id)
    deletebks.delete()
    return redirect('/books')

def membersEdit(request,id): #rendering the edit form with prefilled data for the selected member
    editmembers = Members.objects.get(id=id)
    return render(request, 'edit-members.html', {'memberss':editmembers})

def updateMembers(request,id): #handles form submission and updates the selected member details in the database
    updatemems = Members.objects.get(id=id)
    form = MemberForm(request.POST, instance= updatemems)

    if form.is_valid():
        form.save()
        return redirect('/members')
    else:
        return render(request, 'edit-members.html', {'memberss':updatemems})
    
def membersDelete(request,id): #deletes the selected member details from the database
    deletemems = Members.objects.get(id=id)
    deletemems.delete()
    return redirect('/members')

def borrowersEdit(request,id): #rendering the edit form with prefilled data for the selected borrower

    editborrowers = BorrowersList.objects.get(id=id)
    return render(request, 'edit-borrowers.html', {'borrowerss':editborrowers})

def updateBorrowers(request,id): #handles form submission and updates the selected borrower details in the database
    updatebrws = BorrowersList.objects.get(id=id)
    form = BorrowerForm(request.POST, instance= updatebrws)

    if form.is_valid():
        form.save()
        return redirect('/borrowers')
    else:
        return render(request, 'edit-borrowers.html', {'borrowerss':updatebrws})

def deleteBorrowers(request,id):
    deletebrws = BorrowersList.objects.get(id=id)
    deletebrws.delete()
    return redirect('/borrowers')