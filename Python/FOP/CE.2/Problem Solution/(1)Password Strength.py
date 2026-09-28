psw = input("password: ")
has_digits = False
has_sym = False
has_upper = False
has_lower = False
syms = "!@#$%^&*"

for ch in psw:
    if 'a'<= ch <= 'z':
        has_lower = True
        continue
    if 'A'<= ch <= 'Z':
        has_upper = True
        continue
    if '0' <= ch <= '9':
        has_digits = True
        continue
    if ch in syms:
        has_sym = True
        continue
missing = []
if len(psw) <12:
    missing.append('must be >=12')
if not has_digits:
    missing.append('has digits')
if not has_sym:
    missing.append('has symbols')
if not has_upper:
    missing.append('has uppercase')
if not has_lower:
    missing.append('has lowercase')

if not missing:
    print('strong')
else:
    print('weak')
    for item in missing:
        print('-',item)