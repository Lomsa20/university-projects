def reverse_str(s):
    if s == "": #checks if string is empty or not
        return "" 
    else:
        return reverse_str(s[1:])+ s[0] #put first character at the end while recursing
print(reverse_str("abc"))







