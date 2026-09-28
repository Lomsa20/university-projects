age = int(input("Enter Your Age: "))
hour = int(input("Enter Suitable hour: "))
if age <= 12:
    if hour < 16:
        print("5$")
    else:
        print("7$")
elif 13<age<64 :
    if hour < 16:
        print("10$")
    else:
        print("12$")
elif age :
    if hour <16:
        print("6$")
    else: 
        print("8")
        
        