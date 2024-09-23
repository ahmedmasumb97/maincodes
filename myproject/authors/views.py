from django.shortcuts import render,redirect
from .forms import AuthorForm
from .models import Author
from django.http import HttpResponse
from .import forms

# Create your views here.

def add_author(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_datails')
        else:
            return render(request,'author.html',{'form':form})
    else:
        form = forms.AuthorForm()
        return render(request,'author.html',{'form':form})


def task_list(request):
    task = Author.objects.all()
    data = {
        'task':task
    }
    return render(request,'data_list.html',context=data)


def task_details(request,pk):
    task = Author.objects.get(pk = pk)
    return render(request,'task_details.html',{'task':task})


def delete_task(request,pk):
    try:
        task = Author.objects.get(pk = pk)
        task.delete()
        return redirect('task_list')
    except Author.DoesNotExist:
        return HttpResponse('Task does not exist')

def update_task(request,pk):
    try:
        task = Author.objects.get(pk = pk)
        if request.method == 'POST':
            task_form = AuthorForm(request.POST,instance = task)
            if task_form.is_valid():
                task_form.save()
                print(task_form.cleaned_data)
                return redirect('task_list')
            else:
                return render(request,'update_task.html',{'form':task_form})
        
        task_form = AuthorForm(instance = task)
        return render(request,'update_task.html',{'form':task_form})
    
    except task.DoesNotExist:
        return HttpResponse('task does not exists')



# def size(request):
#     p = Person(nam='Fred Flintstone',Shirt_size='L')
#     p.save()
#     p.name
  
    
# size()



def author_details(request):
    data = Author.objects.all()
    result = []
    # for data in data:
    #     result.append({
    #         'name': data.name,
    #         'bio': data.bio,
    #         'pnone number':data.phone_number
            
    #     })
    return render(request, 'authors_details.html',context={'data':data})