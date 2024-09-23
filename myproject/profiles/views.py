from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProfileForm
from .import forms

# Create your views here.

def add_profile(request):
    if request.method == "POST":
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
       
    else:
        form = forms.ProfileForm
    return render(request, 'add_profile.html',{'form': form})