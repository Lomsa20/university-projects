floor = 0
door_open = False
highest = 0
while True:
    cmd = input().strip()
    if cmd == "Stop":
        break
    parts = cmd.split()
    if not parts:
        continue
    verb = parts[0]
    if verb == "Open":
        door_open = True
    elif verb == "Close":
        door_open = False
    elif verb == "Up" and len(parts) == 2:
        n = int(parts[1])
        if door_open:
            continue
        floor += n
    else:
        pass
print(floor)
print("Open" if door_open else  "Close")
print(highest)


