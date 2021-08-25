from django.shortcuts import render
from uploader.models import Movies
from flix.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
import os
import string
import random
from itertools import groupby



# Create your views here.


def upload(request):
    if(request.method=='POST'):
          name = request.POST.get('name')
          title = request.POST.get('title')
          about = request.POST.get('about')
          category = request.POST.get('category')
          link = request.POST.get('link')
          poster = file_uploader(request.FILES['poster']) 
          c_poster = file_uploader(request.FILES['c_poster'])
          data=Movies(name=name,title=title,about=about,category=category,posterUrl=poster,c_posterUrl=c_poster,link=link)
          data.save()  
    return render (request,'uploader.html')



def file_uploader(file):
    filename=getRandomStr()+file.name  
    path=os.path.join(BASE_DIR, "static/posters/"+filename)
    fs = FileSystemStorage()
    fs.save(path, file)
    return "static/posters/"+filename

def getRandomStr(): 
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return str(res)


def getMovie(category='kid'):
    if(category):
        result = Movies.objects.all().filter(category=category)
    else:
        result = Movies.objects.all()
    return result

def movieDetail(request,movieId):
    try:
        result = Movies.objects.get(id=movieId)
        return render (request,'detailedPage.html',{'data':result})
    except:
        return render (request,'uploader.html')

def movieCategory(request,category):
    try:
        result = Movies.objects.all().filter(category=category)
        print(result)
        return render (request,'category.html',{'data':chunkIt(result,2),'type':category})
    except:
        return render (request,'category.html')

def chunkIt(my_list, n):
    if not(my_list):
        return []
    return [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 
