age = int(input("Age: "))
weight = int(input("Weight(kg): "))
height = float(input("Height(m): "))
BMI = weight / height**2

if age < 18:
    if BMI < 18.5:
        print("underweight(Child)")
    elif 18.5<= BMI <= 24.9:
        print("healthy(Child)")
    else:
        print("overweight(Child)")

if age > 18:
    if BMI < 18.5:
        print("underweight(Adult)")
    elif 18.5 <= BMI <= 24.5:
        print("normal(Adult)")
    elif 25<= BMI < 30:
        print("Overweight(Adult)")
    else:
        print("obese(Adult)")
   
    