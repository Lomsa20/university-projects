# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 11:35:01 2025

@author: mylaptop.ge
"""
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
    
    def __str__(self):
        return f"{self._name} ({self.age}yrs)"
class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self._employee_id = emp_id
        self._salary = salary
    def get_salary(self):
        return self._salary
        
    def __str__(self):
       return f"Employee {self._employee_id} {super().__str__()},Salary: ${self._salary}"
class Department:
    def __init__(self, name):
        self._name = name
        self._employees = []
    def add_employee(self, employee):
        self._employees.append(employee)
        
    def total_salary(self):
        return sum(e.get_salary() for e in self._employees)
    def __str__(self):
        emp_list = "\n ".join(str(e) for e in self._employees)
        return  f"Department: {self._name}\nEmployees:\n{emp_list}\nTotal Salary: ${self.total_salary()}"
#Example usage
dept = Department("IT")
dept.add_employee(Employee("Alice", 30, "E101", 5000))
dept.add_employee(Employee("George", 25, "E102", 4900))
print(dept)


        
