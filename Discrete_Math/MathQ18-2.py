"""
This problem can be solved using various methods, here we will use a loop with additional checks for positive integer solutions.

The problem is to find as many combinations of positive integer values for x, y, and z that fit with the equation x + 2y + 3z = 14.
"""
import math

# Define the equation
equation = "x + 2y + 3z = 14"

Combinations = []

# Loop through different values for x, y, and z
solutions = []  # List to store solutions
for x in range(0, 15):  # Try values from 0 to 14 for x
    for y in range(0, 15):  # Try values from 0 to 14 for y
        for z in range(0, 4):  # Try values from 0 to 3 for z
            # Check if the values satisfy the equation
            if (x + 2 * y + 3 * z == 14) and (x+y+z < 7):
                # Add solution to the list
                solutions.append((x, y, z))
                Combinations.append((math.comb(3, z) * math.comb(6-z, y) * math.comb(6-z-y, x)))

# Print all found solutions
if solutions:
    for solution in solutions:
        print(f"Solution: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
        print(f"Combinations: {Combinations[solutions.index(solution)]}")
    print("Sum of combinations ", sum(Combinations))
else:
    print("No solutions found.")