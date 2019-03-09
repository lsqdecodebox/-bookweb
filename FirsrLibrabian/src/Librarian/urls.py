from django.urls.conf import path
from Librarian import views


urlpatterns = [
    path('',views.librarian,name='Librabian'),
    path('addbook',views.addbook,name='addbook'),
    path('searchbook',views.searchbook,name='searchbook'),
    path('libconduct',views.libconduct,name='libconduct'),
    path('modbook',views.modbook,name='modbook'),
    path('newsedit',views.newsedit,name='newsedit'),
    ]