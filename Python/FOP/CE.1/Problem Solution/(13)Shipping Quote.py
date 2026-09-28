

weight_kg = float(input("Actual weight (kg): "))
l = float(input("Lenght (cm): "))
w = float(input("Width (cm): "))
h = float(input("Height (cm):"))
zone = input("Enter Destination (local,national,international): ").strip() .lower()

is_fragile = input("fragile (yes/no): ").strip() .lower()
is_hazardous = input("hazardous (yes/no): ").strip() .lower()
is_remote = input("remote (yes/no): ").strip() .lower()

dim_weight = (l*w*h)/5000.0
billable = max(weight_kg, dim_weight) 

if zone == "local":
    rate = 2.50
if zone == "national":
    rate = 4.00
if zone == "international":
    rate = 8.00
cost = billable * rate
if is_fragile:
    cost += 6.00
if is_hazardous:
    cost += 12.00
if is_remote:
    cost += 10.00
if billable > 20:
    cost +=15.00

if zone == "local" and billable < 1.0 and cost < 5.0:
    cost = 5.00

if cost > 500:
    cost = 500.0
    print("manual review required")
    
print(f"Shipping quote: ${cost: .4f} (billable weight = {billable: .4f} kg, dim = {dim_weight: .4f} kg)")










