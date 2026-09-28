count = 0
total = 0
max_score = None
min_score = None

while True:
    score = int(input("Enter Score: "))
    if score == -1 :
        break 
    if score > 100 or score < -1 :
        print("invalid score")
        continue
    else:
        total += score
        count += 1
    if max_score is None or score > max_score:
        max_score = score
    if min_score is None or score < min_score:
        min_score = score
if count > 0 :
    avrg = total / count
    print(f"average is {avrg}")
    print(f"total is {total}")
    print(f"count is {count}")
    print(f"max score is {max_score}")
    print(f"min score is {min_score}")
else:
    print("no valid scores enter")

