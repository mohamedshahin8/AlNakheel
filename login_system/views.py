
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import datetime, timedelta, time, date



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



def all_booking(request):

    bookings = Booking.objects.filter(from_date__gte = date.today())
    return render(request, 'all_booking.html', context={'bookings': bookings})

def new_booking(request):
	if request.method == "POST":
		movie_form = MovieForm(request.POST, request.FILES)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, ('Your Booking was successfully added!'))
		else:
			messages.error(request, 'Error saving form')


		return redirect("new_booking")
	movie_form = MovieForm()
	return render(request=request, template_name="new_booking.html", context={'movie_form':movie_form})

def update_booking(request, id):
    booking = Booking.objects.get(booking_id=id)
    if request.method == 'POST':
        movie_form = MovieForm(request.POST,instance=booking)
        if movie_form.is_valid():
            # update the existing `Band` in the database
            movie_form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('all_booking')
    else:
        movie_form = MovieForm(instance=booking)

    return render(request,'update_booking.html',{'movie_form': movie_form})
