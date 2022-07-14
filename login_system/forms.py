from django import forms
from .models import *

class ExpenseForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = '__all__'

class BookingForm(forms.ModelForm):
    disabled_fields = [ 'booking_id', 'booking_source', 'booking_reason' , 'payment_type' ,'customer']
    class Meta:
        model = Booking
        fields = '__all__'
    def __init__(self, *args, **kwargs):
            super(BookingForm, self).__init__(*args, **kwargs)
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                for field in self.disabled_fields:
                    self.fields[field].disabled = True
            # else:
            #     self.fields['reviewed'].disabled = True

class CustomerForm(forms.ModelForm):
    # disabled_fields = [ 'booking_id', 'booking_source', 'booking_reason' , 'payment_type' ,'customer']
    class Meta:
        model = Customer
        fields = '__all__'
    # def __init__(self, *args, **kwargs):
    #         super(MovieForm, self).__init__(*args, **kwargs)
    #         instance = getattr(self, 'instance', None)
    #         if instance and instance.pk:
    #             for field in self.disabled_fields:
    #                 self.fields[field].disabled = True
            # else:
            #     self.fields['reviewed'].disabled = True
