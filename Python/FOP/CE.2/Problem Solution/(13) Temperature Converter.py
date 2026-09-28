a =int(input("a: "))
b = int(input("b: "))
def convert_temp(value, to_celius=False):
    if to_celius == True:
        return (value - 32)*(5/9) # Celsius to Farenheit
    else:
        return value*(9/5) + 32 #Farenhait to celsius
print("C to F: ", convert_temp(a))
print("F to C: ", convert_temp(b, to_celius= True))
