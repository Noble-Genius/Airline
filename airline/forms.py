from django import forms
from .models import Passenger_Info,Flight

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger_Info
        fields = ('name',
                  'email',
                  'gender',
                  'phone',
                  'id_type',
                  'passport'
        )

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ('Airline',
                  'Flying_From',
                  'Flying_To',
                  'Adult',
                  'Child',
                  'Infant'
        )
