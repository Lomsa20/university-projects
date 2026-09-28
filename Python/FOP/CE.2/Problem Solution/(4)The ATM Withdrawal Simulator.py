balance = 500

while balance > 0:

    withdraw = int(input("Amount of withdraw: "))
    while withdraw > 0:
        if withdraw > balance:
            print("Insufficient funds")
        else:
            balance -= withdraw
            print(f"your balance is {balance} ")
        cont = input("Continue(y/n): ") .strip() .lower()
        if cont != "y":
            break
if  balance == 0:
    print("no fund remaining")
        

