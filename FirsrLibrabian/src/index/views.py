from django.shortcuts import render
from django.http.response import HttpResponse
from Librarian.models import Book
from LibNews.models import LibNews

# Create your views here.


def index(request):
    if (request.method == 'POST') and (request.POST.get("search") != ''):
        bookresult = Book.objects.filter(title=request.POST.get("search"))           
    else:
        bookresult = Book.objects.all()
    libnews = LibNews.objects.all()
    return render(request, 'index.html', {'bookresult':bookresult,'libnews':libnews})

