from django.urls.conf import path
from index import views

# app_name = 'index'
urlpatterns = [
    path('',views.index,name = 'index'),
    ]