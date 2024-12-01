from .models import Book ,Members, BorrowersList
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category','quantity','image']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Members
        fields = ['names', 'regNo', 'levels','phoneNumber']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = BorrowersList
        fields = ['names', 'regNo', 'phoneNumber','levels','bkBorrowed','dueDate']