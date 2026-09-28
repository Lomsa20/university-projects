s = "akjabslcsndkjfbdas"
found_at_location = -1
for i in range(len(s)):
    if s[i] == "c":
        found_at_location = i
if found_at_location == -1:
    print("the character 'c' is never found in the string")
else:
    print("the character 'c' is found at position", i)





