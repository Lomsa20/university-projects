num = input("nums: ")
if len(num) < 3:
    print("short") 
else:
    found = False
    for i in range(len(num)-2):
        a,b,c = int(num[i]), int(num[i+1]), int(num[i+2])
        if  b == a+1 and c == b+1:
            found == True
            print(a,b,c)
            break
    if not found :
        print("No pattern")
         
         
     
        



