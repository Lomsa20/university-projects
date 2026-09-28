class Person:
    def __init__(self, name, passport):
        self._name = name
        self._passport = passport

    @property
    def name(self):
        return self._name

    @property
    def passport(self):
        return self._passport


class Pilot(Person):
    def __init__(self, name, passport):
        super().__init__(name, passport)

    def __str__(self):
        return f"Pilot: {self.name} ({self.passport})"


class Passenger(Person):
    def __init__(self, name, passport):
        super().__init__(name, passport)

    def __str__(self):
        return f"Passenger: {self.name} ({self.passport})"


class Flight:
    def __init__(self, flight_no, pilot):
        if not isinstance(pilot, Pilot):
            raise TypeError("Flight pilot must be a Pilot")

        self._flight_no = flight_no
        self._pilot = pilot
        self._passengers = []

    @property
    def flight_no(self):
        return self._flight_no

    def add_passenger(self, passenger):
        if not isinstance(passenger, Passenger):
            raise TypeError("Only Passenger objects can be added")
        if passenger not in self._passengers:
            self._passengers.append(passenger)

    def __str__(self):
        passengers = ", ".join(str(p) for p in self._passengers) or "No passengers"
        return (
            f"Flight: {self._flight_no}\n"
            f"Pilot: {self._pilot}\n"
            f"Passengers: {passengers}"
        )


class Airline:
    def __init__(self, name):
        self._name = name
        self._flights = []

    def add_flight(self, flight):
        if not isinstance(flight, Flight):
            raise TypeError("Only Flight objects allowed")
        self._flights.append(flight)

    def print_schedule(self):
        print(f"Airline: {self._name}")
        for flight in self._flights:
            print(flight)
            print("-" * 30)
