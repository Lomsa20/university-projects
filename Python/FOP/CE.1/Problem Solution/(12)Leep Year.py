y = int(input("Year: "))
m = int(input("Month (1-12): "))
d = int(input("Day: "))

#leap year
leep = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
# Validate month and compute days in month
if m < 1 or m > 12:
    valid = False
else:
    if m == 2:
        
        mdays = 29 if leep else 28
    else:
        # Months 1..7: odd -> 31 (1,3,5,7), even -> 30 (4,6)
        # Months 8..12: even -> 31 (8,10,12), odd -> 30 (9,11)
        if m ==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:  
        
            mdays = 31
        elif m==4 or m==6 or m==9 or m==11:
            mdays = 30
    valid = (1 <= d <= mdays)
if not valid:
    print("invalid date")
else:
    # Quarter
    qnum = (m-1)// 3+1
    quarter = "Q" + str(qnum)
    
    # Meteorological season without lists/tuples
    if m == 12 or m <= 2 :
     season = "Winter"
    elif m <= 5:
        season = "Spring"
    elif m <= 8:
        season = "Summer"
    else:
        season = "Autumn"

    #Boundary
if d == 1:
    boundary = "First day of the month"
elif d == mdays:
    boundary = "last day of the month"
else:
    boundary = "Midle of the month"
        
print(f"valid date: {y:04d}-{m:02d}-{d:02d}")
print(f"quarter: {quarter}")
print(f"season: {season}")
print(f"boundary: {boundary}")

