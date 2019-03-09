from django.forms import ModelForm
#from test.ann_module import Meta
#from django.forms import models
#from django.db.models.fields import CharField
#from django import forms
from .models import Book
from Librarian.models import FirLibAdmin

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class AdminForm(ModelForm):
    class Meta:
        model = FirLibAdmin
        fields = '__all__'