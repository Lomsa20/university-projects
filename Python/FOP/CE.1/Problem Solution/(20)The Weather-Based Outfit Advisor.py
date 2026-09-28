temp = int(input("Enter Temperature(°C): "))
raining = input("is it raining(yes/no)? ") .strip() .lower()
if raining == "yes":
    if temp < 10:
        print(" Wear a raincoat and boots")
    elif 10 <= temp < 20:
        print("Wear a waterproof jacket")
    else:
        print("Wear a light rain poncho")
elif raining =="no":
    if temp < 10:
        print("Wear a warm coat and scarf")
    elif 10 <= temp < 20:
        print("Wear a sweater or hoodie")
    else:
        print("Wear a t-shirt and sunglasses")
else:
    print("invalid input for rain status")
