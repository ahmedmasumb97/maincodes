from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .import forms
from .models import Post

# Create your views here.

def add_post(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            return HttpResponse('Invalid form')
    else:
        form = forms.PostForm()
        return render(request,'add_post.html',{'form':form})





def update_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.PostForm(instance=post)
        return render(request,'update_post.html',{'form':form})


def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('homepage')
  
    