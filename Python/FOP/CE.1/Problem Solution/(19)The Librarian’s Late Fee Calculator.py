book_type = input("Book type fiction/reference): ") .strip().lower()
days_late = int(input("Days late: "))
fee = 0.0 
if days_late <= 0:
    print("no fee")
else:
    if book_type == "fiction":
        if days_late <= 5:
            fee = days_late *0.5
        elif days_late <= 10:
            fee = days_late * 0.75
        else:
            fee = days_late * 1.00
    elif book_type == "reference":
        if days_late <= 5:
            fee =days_late * 1.00
        elif days_late <= 10:
            fee = days_late * 1.50
        else:
            fee = days_late * 2.00
    else:
        print("Unknown book type.")
    print(f"Total late fee: {fee: .3f} $")
