import math
import scipy
from math import factorial
from scipy.special import comb

# def calculate_Kn(m, r, n):
#     # Calculate the probability of getting exactly n kinds of items from m kinds, drawing r times.
#     total_ways = 0
#     for k in range(n + 1):
#         total_ways += (-1)**k * comb(n, k) * (n - k)**r

#     # Multiply by the number of ways to choose n kinds from m kinds.
#     total_ways *= factorial(m) / factorial(m - n)

#     # Divide by the total number of outcomes.
#     probability = total_ways / m**r
#     return total_ways, probability

# # Get user input for m, r, and n
# m = int(input("Enter the total number of kinds (m): "))
# r = int(input("Enter the number of draws (r): "))
# n = int(input("Enter the number of kinds to get (n): "))

# # Calculate the results
# total_ways, probability = calculate_Kn(m, r, n)

# # Print the results
# print(f"Total ways to get exactly {n} kinds from {m} kinds, drawing {r} times: {total_ways}")
# print(f"Probability of K{n}: {probability:.10f}")



## Correct calculation for K5

## Calculate the number of ways to get exactly 5 kinds out of 5 kinds when drawing 6 times
# def calculate_K5(m, r):
#     # Choose which kind is repeated twice
#     choose_repeated_kind = comb(m, 1)
    
#     # Arrange these 5 kinds in 6 spots, considering the repeated kind
#     arrangements = factorial(r) / factorial(2)  # 2! for the repeated kind
    
#     # Total number of outcomes
#     total_outcomes = m**r
    
#     # Calculate the total ways and probability
#     total_ways = choose_repeated_kind * arrangements
#     probability = total_ways / total_outcomes
    
#     return total_ways, probability

# # Inputs
# m = 5  # Total kinds of items
# r = 6  # Number of draws

# # Calculate K5
# total_ways_K5, probability_K5 = calculate_K5(m, r)

# # print (total_ways_K5)
# print (probability_K5)

# def P(m, r, n):
#     result = 0
#     for k in range(n + 1):
#         sign = (-1) ** k
#         binomial_coeff = factorial(n) // (factorial(k) * factorial(n - k))
#         stirling_number = (n - k) ** r
#         factorial_term = factorial(m) // factorial(m - n)
#         result += sign * binomial_coeff * stirling_number * factorial_term
#     return result // (m ** r)

# def K(n, r):
#     result = 0
#     for k in range(n + 1):
#         sign = (-1) ** k
#         binomial_coeff = factorial(n) // (factorial(k) * factorial(n - k))
#         stirling_number = (n - k) ** r
#         result += sign * binomial_coeff * stirling_number
#     return result

# # Example usage
# m = 5  # total number of car types
# r = 6  # total number of draws
# n_values = [1, 2, 3, 4, 5]  # list of n values

# K_values = []
# P_values = []

# for n in n_values:
#     K_values.append(K(n, r))
#     P_values.append(P(m, r, n))

# # Print the results in a table
# print(f"{'n':<10}{'K(n, r)':<10}{'P(m, r, n)':<10}")
# for n, K_val, P_val in zip(n_values, K_values, P_values):
#     print(f"{n:<10}{K_val:<10}{P_val:<10}")


def K(m, r, n):
    result = 0
    for k in range(n + 1):
        sign = (-1) ** k
        binomial_coeff = factorial(n) // (factorial(k) * factorial(n - k))
        stirling_number = (n - k) ** r
        result += sign * binomial_coeff * stirling_number
    return result // (m ** r)

# Example usage
m = 5  # total number of car types
r = 6  # total number of draws
n_values = [5, 4, 3, 2, 1]  # different values of n to calculate K_n

for n in n_values:
    K_n = K(m, r, n)
    print(f"K_{n} = {K_n}")