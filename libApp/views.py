from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Book ,Members ,BorrowersList ,BorrowedBook
from .forms import BookForm , MemberForm ,BorrowerForm 
from django.contrib.auth import authenticate, login ,logout
import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

import json
from django.conf import settings

from .credentials import LipanaMpesaPpassword,MpesaAccessToken
# Create your views here.
def login(request):
    return render(request,'login.html')


def register (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password','').strip()
        confirm_password = request.POST.get('confirm_password','').strip()
        role = request.POST.get('role','student')

        
        if role == 'student':
            print("User registered as a student.")
        elif role == 'librarian':
            print("User registered as a librarian.")

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
    return render(request,'dashboard.html')


def books_view(request):
    query = request.GET.get('query', '')
    if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        results = Book.objects.all()  # Show all books when no search query exists
    
    context = {'bks': results, 'query': query}
    return render(request, 'books-page.html', context)

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
    query = request.GET.get('query', '')
    if query:
        results = Members.objects.filter(names__icontains=query) 
    else:
        results = Members.objects.all()
    context = {'mems':results, 'query': query,'is_search':bool(query)}
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
    query = request.GET.get('query', '')
    if query:
        results = BorrowersList.objects.filter(names__icontains=query) 
    else:
        results = BorrowersList.objects.all()
    context = {'brws':results, 'query': query,'is_search':bool(query)}
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

# @login_required
def studentLib(request): #renders the student library page
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
            return render(request, 'studentLibrarian.html', {'user': user})
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')
            return redirect('login')  # Redirect back to login page

    # If not a POST request, simply show the login page
    return render(request, 'login.html')

def studentBooks(request): # renders the student books page for students to borrow books and  see available books
    query = request.GET.get('query', '')
    if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    else:
        results = Book.objects.all()  # Show all books when no search query exists
    
    context = {'bks': results, 'query': query}
    return render(request, 'studentsBooks.html', context)

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .forms import BorrowBookForm
from .models import Book

def borrow_book(request,id):
    # Get the book by its ID
    book = Book.objects.filter(id=id).first()  
    if not book:
        return redirect('books')  # Redirect if the book doesn't exist

    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            # Get email input
            user_email = form.cleaned_data['email']

            # Render the email confirmation template
            subject = f'Book Borrowed: {book.title}'
            message = render_to_string('email_confirmation.html', {
                'book': book,
                'user': request.user,
            })

            # Send the email
            email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])
            email.content_subtype = 'html'  
            email.send()

            # Redirect to confirmation page if successfull
            return redirect('borrow_confirmation')
    else:
        form = BorrowBookForm()

    # Render the borrow book page with the form and book details
    return render(request, 'borrow_book.html', {'form': form, 'book': book})

def borrow_confirmation(request):
    return render(request, 'borrow_confirmation.html')


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "MMUST library",
            "TransactionDesc": "Fine Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")

def tips(request):
    return render(request, 'tips.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def recommend_books(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        try:
            user = Members.objects.get(names=user_name)
            # Get the last book the user borrowed and liked
            last_borrowed = BorrowedBook.objects.filter(user=user, liked=True).order_by('-borrow_date').first()
            
            if last_borrowed:
                # Find  books in the same category
                similar_books = Book.objects.filter(category=last_borrowed.book.category).exclude(id=last_borrowed.book.id)[:1]
                
                if similar_books.exists():
                    recommended_book = similar_books[0].title
                    message = f"Based on the books you have recently liked and borrowed, we recommend you to try out this one: {recommended_book}"
                else:
                    message = "We couldn't find any similar books to recommend at the moment."
            else:
                message = "We couldn't find any liked books in your history to base a recommendation on."
        except Members.DoesNotExist:
            message = "User not found."
        
        return render(request, 'recommendations.html', {'message': message})
    
    return render(request, 'recommendations.html')
