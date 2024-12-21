size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the pattern using a while loop for rows
while row < size:
    # Use a for loop to print asterisks for each column in the row
    for col in range(size):
        print("*", end="")  # Print without moving to the next line
    print()  # Print a newline after each row
    row += 1
