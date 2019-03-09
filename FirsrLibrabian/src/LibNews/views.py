from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.


def LibNews( request ):
    return HttpResponse('LibNews')
