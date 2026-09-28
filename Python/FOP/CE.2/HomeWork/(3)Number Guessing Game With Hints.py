import random
num = random.randint(1, 100)
attempt = 0
max_attempt = 7

while attempt < 7:
   guess = int(input("n: "))

   if guess == num:
       print("Correct")
       break
   elif guess > num:
       print("Too high")
       
   else:
       print("Too low")
 
   attempt += 1 
   print(f"Attempts lef: {max_attempt - attempt}")

if attempt == max_attempt and guess != num:
    print(f"not found the number{num}")




