from django.shortcuts import render, redirect
from .models import Passenger_Info, Flight
from .forms import PassengerForm, FlightForm

def home(request):
	return render(request, 'index.html')
		
def group_members(request):
	return render (request, 'members.html')
	



def passenger_create(request):
    if request.method != "POST":
        form = PassengerForm()
    else:
        form = PassengerForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        'form1':form
    }
    return render(request, 'new-passenger.html', context)
    

def flight_create(request):
    form = FlightForm
    if request.method != "POST":
        form = FlightForm()
    else:
        form = FlightForm(data=request.POST)
        if form.is_valid():
            
            return redirect("home")
    context = {
        'form2':form
    }



    return render(request, 'flight.html', context)


