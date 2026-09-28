income = float(input("income: "))
if income <= 10**4:
    tax = 0.0
elif (10**4)+1 <= income <= (10**4)*3:
     tax = income * 0.1
     
elif (10**4)*3 + 1 <= income <= 10**5:
     tax = income * 0.2
    
else:
     tax = income * 0.3
print(f"You Taxed by Tax will be {tax: .2f} ")






