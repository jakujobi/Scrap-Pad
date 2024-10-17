from tabulate import tabulate

# Define two lists
list1 = [1, 41, 220, 9020, 9460, 387860, 132440, 678755, 1086008]
list2 = [10000000, 100000, 5000, 100, 100, 7, 7, 4, 3]

# Define the constant
constant = 80089128

# Ensure both lists are of the same length
if len(list1) != len(list2):
    print("Lists are not of the same length. Cannot compute product.")
else:
    # Calculate the intermediate product of the first list and the constant
    intermediate_product = [a/constant for a in list1]

    # Calculate the final product of the intermediate product and the second list
    final_product = [a*b for a, b in zip(intermediate_product, list2)]

    # Prepare the data for the table
    table_data = list(zip(list1, intermediate_product, list2, final_product))

    # Print the result in a table format
    print(tabulate(table_data, headers=["List1 Item", "Intermediate Product", "List2 Item", "Final Product"]))
    #print the sum of all the final products
    print(sum(final_product))