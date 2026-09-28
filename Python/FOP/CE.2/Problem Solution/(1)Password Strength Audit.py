
# first step
psw = input("enter password: ")


has_lower = False
has_upper = False
has_symbol = False
has_digit = False 

symbol = '!@#$%^&*_'

#second step

for ch in psw:
    if 'A' <= ch <= 'Z':
        has_upper = True
    elif 'a' <= ch <= 'z':
        has_lower = True
    elif ch in symbol:
        has_symbol = True
    elif '0' <= ch <= '9':
        has_digit = True      
missing=[]

#third step

if len(psw) < 12:
    missing.append('lenght >= 12')
if not has_digit:
    missing.append('digit')
if not has_lower:
    missing.append('lower cases')
if not has_symbol:
    missing.append('symbols')
if not has_upper:
    missing.append('upper cases')

#last step

if not missing:
    print('Strong password!')
else:
    print('Weak password, missing:')
    for m in missing:
        print('-', m)

    