
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required


# @login_required
def home(request):
    return render(request, 'home.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')


    else:
        return render(request, 'login.html')



def logout_user(request):
    auth.logout(request)
    return redirect('home')
