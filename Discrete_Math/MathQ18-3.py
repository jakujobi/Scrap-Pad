"""
This problem can be solved using various methods, here we will use a loop with additional checks for positive integer solutions.

The problem is to find as many combinations of positive integer values for x, y, and z that fit with the equation x + 2y + 3z = 5.
"""

# Define the equation
equation = "x + 2y + 3z = 5"

# Loop through different values for x, y, and z
solutions = []  # List to store solutions
for x in range(0, 10):  # Try values from 0 to 5 for x
    for y in range(0, 10):  # Try values from 0 to 5 for y
        for z in range(0, 10):  # Try values from 0 to 5 for z
            # Check if the values satisfy the equation
            if x + 2 * y + 3 * z == 5:
                # Add solution to the list
                solutions.append((x, y, z))

# Print all found solutions
if solutions:
    for solution in solutions:
        print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
else:
    print("No solutions found.")