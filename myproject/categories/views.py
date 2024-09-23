from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CatagoryForm
from .import forms


# Create your views here.

def add_catagory(request):
    if request.method == 'POST':
        form = forms.CatagoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        else:
            return render(request,'author.html',{'form':form})
    else:
        form = forms.CatagoryForm()
        return render(request,'catagories.html',{'form':form})