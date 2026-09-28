# Read version-like inputs from the user, e.g., "2.10.3"
A = input("A (e.g. 2.10.3): ")
B = input("B (e.g. 2.10.3): ")

# Split the strings into separate parts by the dot "."
# This gives the major, minor, and patch versions as strings
A1s, A2s, A3s = A.split(".")
B1s, B2s, B3s = B.split(".")

# Convert each string part to integers for comparison
A1, A2, A3 = int(A1s), int(A2s), int(A3s)
B1, B2, B3 = int(B1s), int(B2s), int(B3s)

# Compare the versions piece by piece

# Check if A is greater than B
# A is greater if:
#  - its major version is bigger, OR
#  - major versions are equal and minor is bigger, OR
#  - major and minor equal and patch is bigger
gt = (A1 > B1) or (A1 == B1 and A2 > B2) or (A1 == B1 and A2 == B2 and A3 > B3)

# Check if A is less than B (similar logic, just reversed)
lt = (A1 < B1) or (A1 == B1 and A2 < B2) or (A1 == B1 and A2 == B2 and A3 < B3)

# Check if A is exactly equal to B
# All three parts must be equal for versions to be the same
eq = (A1 == B1) and (A2 == B2) and (A3 == B3)

# Decide and print the result
if gt:
    print("A is greater than B")
elif eq:
    print("A is equal to B")
else:  # if not greater and not equal, then it must be less
    print("A is less than B")



