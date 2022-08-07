from django.db import models
from datetime import datetime, timedelta, time, date

#CREATE YOUR CHOICES
SOURCE_CHOICES=(
    ('Booking.com' , 'Booking.com'),
)
REASONS_CHOICES=(
    ('Tourism' , 'Tourism'),
)
PAYMENT_CHOICES=(
    ('Cash' , 'Cash'),
    ('Visa' , 'Visa'),
)

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Floor(models.Model):
    floor_id = models.AutoField(primary_key=True)
    floor_name = models.CharField(max_length=20)
    floor_rooms = models.CharField(max_length= 20)

    def __str__(self):
        return f"{self.floor_name}"



class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=20)
    floor_name = models.ForeignKey( Floor , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room_name}"



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    social_id = models.CharField(max_length = 10)
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length = 10)
    full_name = models.CharField(max_length = 40)
    contact_number = models.CharField(max_length= 11)
    contact_email = models.CharField(max_length= 40)
    gender = models.CharField(max_length= 10)
    country = models.ForeignKey(Country,on_delete = models.CASCADE)
    # city name for egypt only
    city = models.ForeignKey(City, on_delete= models.CASCADE)
    member_creation_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.customer_id}"





class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    booking_source = models.CharField(max_length= 15,choices=SOURCE_CHOICES)
    booking_reason = models.CharField(max_length= 15,choices=REASONS_CHOICES)
    customer = models.CharField(max_length = 20)
    accompanied_with = models.CharField(max_length = 20, null= True,blank=True)
    total_guests = models.IntegerField(default= 1)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    # payment_type = models.CharField(max_length= 15,choices=PAYMENT_CHOICES)
    from_date = models.DateTimeField(default=datetime.now)
    to_date = models.DateTimeField(default=datetime.now)
    total_amount = models.IntegerField()
    # paid_amount = models.IntegerField()
    notes = models.CharField(max_length= 1000 , null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.booking_id}"

    # @property
    # def Pending_amount(self):
        # pending_amount = self.total_amount - self.paid_amount
        # return pending_amount
    # @property
    # def Collected_amount()



class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



class Expense(models.Model):
    """docstring for Expense."""
    expense_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    item = models.ForeignKey(Item,on_delete = models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    expense_price = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.expense_id}"
