from tabulate import tabulate
import math

OptionsList = [365, 365, 365, 12, 7, 365, 12, 7, 37]
Individuals = [29,  34,   3,   3, 2,  5,  5,  5, 10]

# Individuals ** OptionsList
power_list = [i**o for i, o in zip(Individuals, OptionsList)]

# Individuals Permutation OptionsList (IpO)
permutation_list = [math.perm(o, i) for i, o in zip(Individuals, OptionsList)]

# (Individuals ** OptionsList) - (Individuals Permutation OptionsList (IpO))
difference_list = [p - perm for p, perm in zip(power_list, permutation_list)]

# (Individuals ** OptionsList) - (Individuals Permutation OptionsList (IpO)) / (Individuals ** OptionsList)
division_list = [diff / p if p != 0 else 0 for diff, p in zip(difference_list, power_list)]

# Prepare data for the table
table = zip(OptionsList, Individuals, power_list, permutation_list, difference_list, division_list)

# Print the table with 5 significant digits
formatted_table = [[f"{value:.5g}" for value in row] for row in table]
print(tabulate(formatted_table, headers=["Options", "Individuals", "Individuals^Options", "Permutations", "Difference", "Division"], tablefmt="grid"))