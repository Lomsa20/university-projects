# Ask the user to enter the number of rows for the matrix
rows = int(input("row: "))

# Ask the user to enter the number of columns for the matrix
cols = int(input("cols: "))

# Create an empty list that will hold all rows of the matrix.
# Each row itself will be a list of integers.
matrix = []

# This loop will run 'rows' times — once for each row of the matrix
for i in range(rows):

    # Ask the user to enter all elements for the current row, separated by spaces.
    # Example input: "1 2 3"
    # The input() function returns a string, so we split it into separate parts.
    # .split() splits the string by spaces into a list of substrings → ['1', '2', '3']
    # map(int, ...) converts each substring into an integer → [1, 2, 3]
    # list(...) turns the map object into a list of integers.
    row = list(map(int, input(f"enter row {i+1}: ").split()))

    # Append the newly created list 'row' into the main matrix list.
    # After this, 'matrix' becomes a list of lists (2D structure).
    matrix.append(row)

# After the loop, the matrix looks like this (for example):
# If rows=2 and cols=3 and user entered:
#   1 2 3
#   4 5 6
# Then matrix = [[1, 2, 3], [4, 5, 6]]

# Print a header message so the user knows what’s coming next
print("transposed matrix: ")

# The next two nested loops will print the transposed version of the matrix.
# A transpose means rows become columns and columns become rows.

# Outer loop goes through each column index (0 up to cols-1)
for j in range(cols):

    # Inner loop goes through each row index (0 up to rows-1)
    for i in range(rows):

        # Print the element located at row i and column j of the original matrix.
        # Since we are looping by column first (j) and row second (i),
        # we’re effectively swapping their positions.
        # Example: matrix[i][j] (original) becomes matrix[j][i] (transposed position)
        print(matrix[i][j], end=" ")

    # After printing one entire "row" of the transposed matrix,
    # print a newline so the next transposed row starts on a new line.
    print()

