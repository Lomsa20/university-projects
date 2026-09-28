age =int(input("Age: "))
day_type = input("weekday/weekend: ").strip() .lower()
hour = float(input("hour: "))
is_student = input("student(yes/no): ").strip() .lower()

if age < 0 or hour < 0 or hour > 23 or (day_type not in ("weekday", "weekend")):
    print("invalid")                                        

price = 12

if 17 <= hour < 22:
    price += 2 
    if day_type == "weekend":
        price += 3
else:
    price = 12

if age <= 12:
    price -= 4
elif age >= 65:
    price -= 3
if is_student == "yes":
    price -= 2
if price < 5:
    price = 5

print(f"Amount to pay: {price: .2f} $")


