from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Expense)
admin.site.register(Room)
admin.site.register(Floor)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Item)
class PaymentLineAdmin(admin.ModelAdmin):
    list_display = ['booking_id','booking_amount' , 'total_amount', 'amount']

admin.site.register(PaymentLine,PaymentLineAdmin)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_id', 'booking_id', 'booking_amount', 'paid_amount', 'num_paid' ]

admin.site.register(Payment , PaymentAdmin)
