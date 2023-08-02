from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout as log_out
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  
  return render(request, "home.html")

def logout(request):
  log_out(request)
  return redirect('login')

def index(request):
  if request.method == 'POST':
      lv = LoginForm(request.POST)
      if lv.is_valid():
        username = request.POST.get("username")
        password = request.POST.get('password')      
        user  = authenticate(username=username, password=password)
        if user:
          login(request, user)
          return redirect("home")
        else:
          messages.error(request, "Invalid user or password")
          return redirect("login")
          
  context ={
    'form':LoginForm(),
  }
  return render(request, "accounts/login.html",context)
