score = int(input("Score: "))


if 90 <= score <= 100:
    print("you get highest Score A")
elif 80 <= score <= 89:
    print("you get B")
elif 70 <= score <= 79:
    print("you get C")
elif 60 <= score <= 69:
    print("you get D")
elif 0 <= score <= 59:
    print("you get F")
else:
    print("invalide score")
