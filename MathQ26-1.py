import math
import scipy
from math import factorial
from scipy.special import comb

def calculate_Kn(m, r, n):
    # Calculate the probability of getting exactly n kinds of items from m kinds, drawing r times.
    total_ways = 0
    for k in range(n + 1):
        total_ways += (-1)**k * comb(n, k) * (n - k)**r

    # Multiply by the number of ways to choose n kinds from m kinds.
    total_ways *= factorial(m) / factorial(m - n)

    # Divide by the total number of outcomes.
    probability = total_ways / m**r
    return total_ways, probability

# Get user input for m, r, and n
m = int(input("Enter the total number of kinds (m): "))
r = int(input("Enter the number of draws (r): "))
n = int(input("Enter the number of kinds to get (n): "))

# Calculate the results
total_ways, probability = calculate_Kn(m, r, n)

# Print the results
print(f"Total ways to get exactly {n} kinds from {m} kinds, drawing {r} times: {total_ways}")
print(f"Probability of K{n}: {probability:.10f}")
