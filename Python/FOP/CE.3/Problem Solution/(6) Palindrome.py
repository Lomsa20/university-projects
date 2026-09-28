def _palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]: #logic here is if first != LAst then return False
    
        return False
    else:
        return _palindrome(s[1:-1])
print(_palindrome("abcba"))








