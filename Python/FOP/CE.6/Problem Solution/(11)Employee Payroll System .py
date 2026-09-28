class PayRoll:
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must override this method")
class FullTimeEmployee(PayRoll):
    def __init__(self,monthly_salary):
        self._monthly_salary = monthly_salary
    def calculate_salary(self):
        return self._monthly_salary
class PartTimeEmployee(PayRoll):
    def __init__(self,hour,sph): #salary per hour
        self._hour = hour
        self._sph = sph
    def calculate_salary(self):
        return self._hour * self._sph
class Contractor:
    def __init__(self,project_fee):
        self._project_fee = project_fee
    def calculate_salary(self):
        return self._project_fee
employee = [FullTimeEmployee(1500), PartTimeEmployee(6,10), Contractor(1000)]
for e in employee:
    print(f"Executing: {e.calculate_salary()}")