from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.core.files.storage import FileSystemStorage

from .forms import BookForm
from .models import Book

# Create your views here.


def home(request):
    return render(request,'home.html')

def upload(request):
    return render(request,'upload.html')

def book_list(request):
    books =Book.objects.all()
    return render(request,'book_list.html',{
        'books':books
    })

def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'upload_book.html',{
        'form':form
    })

def delete_book(request,pk):
    if request.method=='POST':
        book=Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


