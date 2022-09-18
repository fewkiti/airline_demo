from django.test import TestCase
from .models import Airport, Flight, Passenger


class FlightTestCase(TestCase):

    def setUp(self):

        # create airports
        airport1 = Airport.objects.create(code="AAA", city="City A")
        airport2 = Airport.objects.create(code="BBB", city="City B")

        Flight.objects.create(
            origin=airport1, destination=airport2, duration=400)

    def test_seat_available(self):
        """ is_seat_available should be True """

        flight = Flight.objects.first()

        self.assertTrue(flight.is_seat_available())

    def test_seat_not_available(self):
        """ is_seat_available should be False """

        passenger1 = Passenger.objects.create(
            first="harry", last="potter")
        passenger2 = Passenger.objects.create(
            first="hermione", last="granger")

        flight = Flight.objects.first()
        flight.passengers.add(passenger1)
        flight.passengers.add(passenger2)

        self.assertFalse(flight.is_seat_available())
