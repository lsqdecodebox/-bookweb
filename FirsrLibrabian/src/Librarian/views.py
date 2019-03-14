from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from Librarian.forms import BookForm, AdminForm
from Librarian.models import FirLibAdmin, Book
from django.contrib import messages
from LibNews.models import LibNews
from LibNews.forms import NewsForm
from django.contrib.admin import models
from django.contrib.auth.decorators import login_required


# def my_login_required(func):
#     '''自定义 登录验证 装饰器'''
#     def check_login_status(request):
#         '''检查登录状态'''
#         if request.session.has_key('user_id'):
#             # 当前有用户登录，正常跳转
#             return func(request)
#         else:
#             # 当前没有用户登录，跳转到登录页面
#             return HttpResponseRedirect('/login')
#     return check_login_status
#@login_required
def addbook(request):
    if request.method == 'POST':
        Form = BookForm(request.POST)
        if Form.is_valid():
            book = Form.save()
            book.save()
            messages.success(request,'book saved !')
    else:
        Form = BookForm()
    return render(request, 'Librarian/addbook.html')


def librarian( request ):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = FirLibAdmin.objects.get(name=username)
                if user.password == password:
                    return redirect('libconduct')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'Librarian/Librarian.html', {"message": message})
    return render(request, 'Librarian/Librarian.html')



def libconduct(request):
    if (request.method == 'POST') and (request.POST.get("search") != ''): 
        bookresult = Book.objects.filter(title__contains=request.POST.get("search"))
    else:
        bookresult = Book.objects.all()
    return render(request, 'Librarian/libconduct.html', {'bookresult':bookresult})

def modbook(request):
    if (request.method == 'POST') and (request.POST.get("nid")):
        if request.POST.get("title"):
            Form = BookForm(request.POST)
            if Form.is_valid():
                book = Book()
                book.price=request.POST.get("price",None)
                book.title=request.POST.get("title",None)
 #               book.pub_date=request.POST.get("pub_date",None)
                book.publish=request.POST.get("publish",None)
                book.authors_name=request.POST.get("authors_name",None)
                book.link=request.POST.get("link",None)
                Book.objects.filter(nid=request.POST.get("nid")).update(price=book.price,title=book.title,
                                                                        pub_date=book.pub_date,publish=book.publish,
                                                                        authors_name=book.authors_name,link=book.link)
                messages.success(request,'book changed !') 
                bookalter= Book.objects.get(nid=request.POST.get("nid"))
                return render(request, 'Librarian/modbook.html', {'bookalter':bookalter} )
        else:        
            bookalter = Book.objects.get(nid=request.POST.get("nid"))
            return render(request, 'Librarian/modbook.html', {'bookalter':bookalter})
    else:
        return redirect('libconduct')

def deletebook(request):
    if request.method=='POST' and request.POST["nid"]:
        Book.objects.get(nid=request.POST.get("nid")).delete()
        messages.success(request,'book deleted !') 
    return redirect('modbook')
     

def searchbook(request):  
    if (request.method == 'POST') and (request.POST.get("search") != ''):
        bookresult = Book.objects.filter(title__contains=request.POST.get("search"))           
    else:
        bookresult = Book.objects.all()
    return render(request, 'Librarian/searchbook.html', {'bookresult':bookresult})
        
def newsedit(request):
    if request.method =='POST' :
        Form = NewsForm(request.POST)
        if Form.is_valid():
            news = Form.save()
            news.save()
    newstable = LibNews.objects.all()
    return render(request, 'Librarian/newsedit.html', {'newstable':newstable})
        