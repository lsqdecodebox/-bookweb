from django.urls.conf import path
from LibNews import views

urlpatterns = [
    path('',views.LibNews,name='LibNews'),
    ]