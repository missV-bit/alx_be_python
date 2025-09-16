# pattern_drawing.py

# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for each row
while row < size:
    # Nested for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to next line after row
    row += 1
