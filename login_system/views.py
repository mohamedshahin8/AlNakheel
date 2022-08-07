
# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import datetime, timedelta, time, date
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404




# @login_required
def home(request):
    return render(request, 'home.html')

#LOGIN VIEW
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


#LOGOUT VIEW
def logout_user(request):
    auth.logout(request)
    return redirect('home')

#ALL CUSTOMERS VIEW
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'all_customers.html', context={'customers': customers})

#CUSTOMER DETAILS VIEW
def customer_details(request, id):
    customers = Customer.objects.get(customer_id = id)
    return render(request, 'customer_details.html', context={'customers': customers})

def new_customer(request):
	if request.method == "POST":
		customer_form = CustomerForm(request.POST, request.FILES)
		if customer_form.is_valid():
			customer_form.save()
			messages.success(request, ('Customer was successfully added!'))
		else:
			messages.error(request, 'Error saving form')


		return redirect("customers")
	customer_form = CustomerForm()
	return render(request=request, template_name="new_customer.html", context={'customer_form':customer_form})

def bookings(request):
    return render(request, 'bookings.html')

def all_booking(request):
    bookings = Booking.objects.filter(from_date__gte = date.today())
    # bookings = Booking.objects.filter(from_date__gte = date.today())
    updated_bookings = Booking.objects.filter(updated_at__gte = date.today())
    return render(request, 'all_bookings.html', context={'bookings': bookings , 'updated_bookings' : updated_bookings})

def new_booking(request):
	if request.method == "POST":
		booking_form = BookingForm(request.POST, request.FILES)
		if booking_form.is_valid():
			booking_form.save()
			messages.success(request, ('Your Booking was successfully added!'))
		else:
			messages.error(request, 'Error saving form')


		return redirect("new_booking")
	booking_form = BookingForm()
	return render(request=request, template_name="new_booking.html", context={'booking_form':booking_form})

def update_booking(request, id):
    booking = Booking.objects.get(booking_id=id)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST,instance=booking)
        if booking_form.is_valid():
            # update the existing `Band` in the database
            booking_form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('all_booking')
    else:
        booking_form = BookingForm(instance=booking)

    return render(request,'update_booking.html',{'booking_form': booking_form})



def expenses(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses.html', context={'expenses': expenses})


def new_expense(request):
    expense_form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if expense_form.is_valid():
            expense_form.save()
            return redirect('expense_add')
    return render(request, 'new_expense.html', {'expense_form': expense_form})




# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

# AJAX
def load_items(request):
    category_id = request.GET.get('category_id')
    items = Item.objects.filter(category_id=category_id).all()
    return render(request, 'item_dropdown_list_options.html', {'items': items})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def search_customers(request):
    if request.method == "POST":
        searched = request.POST['searched']
        customer = Customer.objects.filter(full_name__contains= searched)
        return render(request, 'search_customer.html', {'searched' : searched , 'customer' : customer})
    else:
        return render(request, 'search_customer.html')
