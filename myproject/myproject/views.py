
from posts.models import Post
from categories.models import Catagory
from django.shortcuts import render, redirect
# Create your views here.
def category(request):
   data = Catagory.objects.all()
   print(data)
   return render(request, 'home.html',{'category': data})

def home(request):
   data = Post.objects.all()
   return render(request, 'home.html',{'data': data})

   