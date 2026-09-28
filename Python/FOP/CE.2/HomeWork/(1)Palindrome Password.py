pwd = input("pwd: ").strip()

has_pal = pwd == pwd[::-1]
has_len = len(pwd) >= 6
if has_pal  and has_len:
    has_pal = True
    print("Valid Palindrome Password")
else:
    if not has_pal:
        print("invalid it must be palindrom")
    if not has_len:
        print("invalid length must be greater then 6")
    

