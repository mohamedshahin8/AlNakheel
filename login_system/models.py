from django.db import models
from datetime import datetime, timedelta, time, date

# Create your models here.

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    mobile_number = models.IntegerField()

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, primary_key=True)
    social_id = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    full_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length= 11)
    contact_email = models.CharField(max_length= 40)
    gender = models.CharField(max_length= 10)
    country_name = models.CharField(max_length = 15)
    # city name for egypt only
    city_name = models.CharField(max_length = 10)
    member_creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.customer_id}"

class Movie(models.Model):
	movie_title = models.CharField(max_length=150)
	release_year = models.IntegerField()
	director = models.CharField(max_length=100)
	# movie_poster = models.ImageField(upload_to='images/', None=True)
	movie_plot = models.TextField()


	def __str__(self):
		return self.movie_title

class Booking(models.Model):
    booking_id = models.CharField(max_length=20, primary_key=True)
    booking_source = models.CharField(max_length= 15)
    booking_reason = models.CharField(max_length= 15)
    customer = models.CharField(max_length = 30)
    payment_type = models.CharField(max_length= 15)
    from_date = models.DateTimeField(auto_now_add=True)
    to_date = models.DateTimeField(default=datetime.now)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    pending_amount = models.IntegerField()

    def __str__(self):
        return f"{self.booking_id}"

class Floor(models.Model):
    floor_id = models.CharField(max_length=20, primary_key=True)
    floor_name = models.CharField(max_length=20)
    floor_rooms = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.floor_name}"

class Expense(models.Model):
    """docstring for Expense."""
    expense_id = models.CharField(max_length=20, primary_key=True)
    expense_category = models.CharField(max_length= 20)
    expense_item = models.CharField(max_length= 25)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    expense_price = models.IntegerField()

    def __str__(self):
        return f"{self.expense_id}"


class Room(models.Model):
    room_id = models.CharField(max_length=20, primary_key=True)
    room_name = models.CharField(max_length=20)
    floor_name = models.ForeignKey( Floor , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room_name}"
