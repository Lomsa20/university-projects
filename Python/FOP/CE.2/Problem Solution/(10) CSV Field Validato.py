line = input("csv: " )
field = line.split(", ")
valid_count = 0
first_invalid = -1
for i, f in enumerate(field):
    if f =="":
        first_invalid =  i if first_invalid == -1 else first_invalid # if f =="": set first_invalid  if not set; continue        
        continue
    if f!= f.strip():
        first_invalid = i if first_invalid == -1 else first_invalid #  If f != f.strip(): leading/trailing spaces → mark invalid; continue
        continue
    valid_count += 1
print(valid_count)
print(first_invalid)