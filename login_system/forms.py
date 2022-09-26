from django import forms
from .models import *

class ExpenseForm(forms.ModelForm):
  class Meta:
    model = Expense
    fields = '__all__'

class InvoiceForm(forms.ModelForm):
  class Meta:
    model = Payment
    fields = '__all__'

class BookingForm(forms.ModelForm):
    disabled_fields = ['booking_source', 'booking_reason' ,'customer','accompanied_with' , 'total_guests' , 'room','total_amount']
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
    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
    # def __init__(self, *args, **kwargs):
    #         super(MovieForm, self).__init__(*args, **kwargs)
    #         instance = getattr(self, 'instance', None)
    #         if instance and instance.pk:
    #             for field in self.disabled_fields:
    #                 self.fields[field].disabled = True
            # else:
            #     self.fields['reviewed'].disabled = True
