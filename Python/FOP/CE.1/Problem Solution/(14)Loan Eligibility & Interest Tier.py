income = int(input("Income: "))
credit = int(input("credit: "))
years_job = float(input("how many Year do you work at same job: "))
has_collateral = input("Collateral provoided(yes/no): ").strip() .lower()

if income < 15*10**3 or credit < 58*10:
    print("not eligble")
else:
    if 580 <= credit <= 619:
        rate = 9.5
    elif 620 <= credit <=679:
        rate = 7.0
    elif 680 <= credit <= 749:
        rate = 5.5
    else:
        rate = 4.0
if years_job >= 2:
    rate -= 0.5
if has_collateral == "yes":
    rate -= 0.25
if rate < 3.5:
    rate = 3.5


print(f"Eligible interest rate is {rate: .3f} %")








