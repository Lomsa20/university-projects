cpwd = "OpenSesame"
attempt = 0
while attempt < 3:
    pwd = input('enter password: ')
    if pwd == "OpenSesame":
        print("Accesss granted")    
        break
    else: 
        attempt +=1
        print("inccorect password")
if attempt == 3:
    print("Account locked")