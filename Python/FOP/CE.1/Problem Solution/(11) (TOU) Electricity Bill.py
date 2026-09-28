kwh = float(input("kwh: "))
day_type = input("Enter(weekday/weekend): ")
hour = int(input("hour: "))

# Tiered charge
if 0 <= kwh <= 150:
   charge = kwh * 0.12
elif 150 < kwh <= 500:
    charge = 150 * 0.12 + (kwh-150) * 0.20
else:
    charge = 150 * 0.12 + 350 * 0.20 + (kwh-500) * 0.28
    
#Tou multiplier
if day_type == "weekday":
    if 17 <= hour <= 22:
        mult = 1.25
    elif (7<= hour <=17) or (22 <= hour <= 24):
        mult = 1.10
    else:
        mult = 1.00
        
elif day_type == "weekend":
    mult = 0.95

else:
    print("invalid day type; assuming weekday baseline.")
    mult = 1.00
bill = charge * mult

#Lifeline credit and floor at zero
if kwh <= 120:
    bill -= 8
if bill < 0:
    bill = 0.0
print(f"Final Bill: ${bill: .4f}")
if bill > 200:
    print("Warning")    

    







