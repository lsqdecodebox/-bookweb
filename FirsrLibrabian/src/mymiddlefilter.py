# -*- coding: utf-8 -*-
from django.conf import settings
from re import compile
from django.http import HttpResponseRedirect
 
EXEMPT_URLS=[compile(settings.LOGIN_URL.lstrip('/'))]
 
# if hasattr(settings,'LOGIN_EXEMPT_URLS'):
#     EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]
 
class LoginRequiredMiddleware:
 
    def process_request(self, request):
        if 'user' not in request.session or not request.session['user']:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                # print path
                ['Librarian/libconduct.html',
                 'Librarian/modbook.html',
                 'Librarian/newsedit.html',
                 'Librarian/addbook.html',
                 ]
                return HttpResponseRedirect('Librarian/Librarian.html')
