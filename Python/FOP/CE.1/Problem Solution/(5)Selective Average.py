x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: ")) 

# Create mask variables (mx, my, mz)
# Each mask is 1.0 if the number is positive, otherwise 0.0
# This lets us include only positive numbers in our calculations.

mx = float(x > 0.0)
my = float(y > 0.0)
mz = float(z > 0.0)


# Count how many numbers are positive
# Since each mask is either 1.0 (positive) or 0.0 (not positive),
# adding them gives the total count of positive values.

count = mx + my + mz

# Calculate the sum of only the positive numbers
# If a number is not positive, its mask will be 0.0, so it won't affect the total.

total = x*mx + y*my + z*mz

# Compute the average of positive numbers.
# If count == 0, float(count != 0.0) becomes 0.0, making the average 0.0 automatically.
# This prevents a "division by zero" error.

average = (total / count) * float(count != 0.0)

print(int(count))
print(average)
    
    


