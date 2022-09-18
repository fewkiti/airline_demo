from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.


def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })


def flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight)
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = get_object_or_404(Flight, pk=flight_id)
        passenger = get_object_or_404(Passenger, pk=int(request.POST["passenger"]))
        if passenger not in flight.passengers.all() and flight.is_seat_available():
            passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
            passenger.flights.add(flight)
            # flight.passengers.add(passenger)
    return HttpResponseRedirect(reverse("flights:flight", args=(flight.id,)))
