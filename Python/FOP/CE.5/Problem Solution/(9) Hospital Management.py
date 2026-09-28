class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
class Doctor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f'Doctor {self.name} at {self.age} years old'
class Patient(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    def __str__(self):
        return f'Patient {self.name} at {self.age} years old'
class Appointment:
    def __init__(self, doctor, person, time):
        self._doctor = doctor
        self._person = person
        self._time = time
    @property
    def doctor(self):
        return self._doctor
    @property
    def person(self):
        return self._person
    @property
    def time(self):
        return self._time
    def __str__(self):
        return f'Appointment at {self._time} \n doctor: {self._doctor} \n person: {self._person}'
class Hospital:
    def __init__(self):
        self._appointments = []
    def schedule(self, appointment):
        self._appointments.append(appointment)
    def __str__(self):
        return "Appointments:\n" + "\n".join(str(a) for a in self._appointments)
    