class Employee:
    def calculate_salary(self):
        raise NotImplementedError("Subclasses must implement calculate_salary")


class FullTime(Employee):
    def __init__(self, monthly_salary):
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary


class PartTime(Employee):
    def __init__(self, hourly_rate, working_hours):
        self._hourly_rate = hourly_rate
        self._working_hours = working_hours

    def calculate_salary(self):
        return self._hourly_rate * self._working_hours


class Contractor(Employee):
    def __init__(self, contract_amount):
        self._contract_amount = contract_amount

    def calculate_salary(self):
        return self._contract_amount


class Team:
    def __init__(self):
        self._employees = []

    def __add__(self, other):
        if not isinstance(other, Employee):
            raise TypeError("Can only add Employee to Team")
        self._employees.append(other)
        return self  # allows chaining: team + emp1 + emp2
    def total_salary(self):
        return sum(emp.calculate_salary() for emp in self._employees)
class Department:
    def __init__(self):
        self._teams = []
    def add_team(self,team):
        if not isinstance(team, Team):
            raise TypeError("Can only add Department to Team")
        self._teams.append(team)
    def total_salary(self):
        return sum(team.total_salary() for team in self._teams)
team1 = Team() + FullTime(3000) + PartTime(20, 80)
team2 = Team() + Contractor(2000)

dept = Department()
dept.add_team(team1)
dept.add_team(team2)

print(dept.total_salary())  # 3000 + 1600 + 2000 = 6600
