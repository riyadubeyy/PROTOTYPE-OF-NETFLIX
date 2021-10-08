from contextlib import contextmanager
from flix.settings import INSTALLED_APPS
from typing import ContextManager
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect, request

# Create your views here.
def netflix(request):
    return render (request,'netflix.html')

def login(request):
     return render (request,'login.html')

def home(request):
     return render (request,'home.html')
  
def about(request):
    return render (request,'about.html')

def spidermannwh(request):
    return render (request,'spidermannwh.html')





    

    