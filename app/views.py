
from .models import todomodel
from django.contrib.auth import authenticate, logout,login as loginuser
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

from .form import todoform,SignUpForm  


#@login_required(redirect_field_name='login')
def home(request):
    if request.user.is_authenticated:
        user=request.user
        form=todoform()
        todos=todomodel.objects.filter(user=user).order_by('Priority')
        return render(request,'app/home.html',{"form":form,'todos' : todos})
    else:
        return redirect('login')
        
    

def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        return render(request,'app/login.html',{"form":form})
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
                
        else:
            return render(request,'app/login.html',{"form":form})
    return render(request,'app/login.html')


def signup(request):
    if request.method=='GET':
        form=SignUpForm()
        return render(request,'app/signup.html',{"form":form})

    else:
        form=SignUpForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            if user is not None:
                return redirect('login')
            
        else:
            return render(request,'app/signup.html',{"form":form}) 


def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(request.user)
        form=todoform(request.POST)
        if form.is_valid():
            todos=form.save(commit=False)
            todos.user=user 
            todos.save()
            return redirect("home")
        else:
            return render(request,'app/home.html',{"form":form})

def signout(request):
    logout(request)
    return redirect("login")

def delete(request,pk):
    todomodel.objects.get(pk=pk).delete()
    return redirect("home")

def change_todo(request , id  , status):
    todo = todomodel.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')

