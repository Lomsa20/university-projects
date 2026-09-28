pwd =input("Enter password: ")

#Helper flags -- these start as False, meaning:
## we *haven’t yet found* any uppercase, lowercase, digit, or symbol in the password.
has_upper = False # Will become True if the password has at least one uppercase letter (A–Z)
has_lower = False  # Will become True if it has at least one lowercase letter (a–z)
has_digit = False # Will become True if it has at least one number (0–9)
has_symbol = False # Will become True if it has at least one symbol from "!@#$%^&*"

symbols = "!@#$%^&*"
 
# Loop through each character in the entered password
for ch in pwd:
    if 'A' <= ch <= 'Z': # Check if it's an uppercase letter
        has_upper = True 
    elif 'a'<= ch <= 'z': # Check if it's a lowercase letter
        has_lower = True
    elif '0' <= ch <= '9': # Check if it's a digit
        has_digit = True
    elif ch in symbols: # Check if it's one of the allowed symbols
        has_symbol = True

if len(pwd) < 6:
    classification = "invalid"
else:
    if ' ' in pwd:
        classification = "invalid"
    else:
        low = pwd.lower()
        if low == "password" or low == "123456" or low =="qwerty":
            classification = "invalid"
        else:
            #Valid --> determine strength
            classification = "Weak"
            if len(pwd) >= 8 and has_digit:
                classification = "Moderate"
            if len(pwd) >= 10 and has_upper and has_lower and has_digit:
                classification = "Strong"
                if len(pwd) >= 12 and has_symbol: #Here i also can use elif function but this will work also
                    classification = "Strongest"
print(f"Password strength: {classification}")
                



