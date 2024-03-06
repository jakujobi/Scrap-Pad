from tabulate import tabulate

# Define two lists
list1 = [1, 18, 210, 3780, 8610, 154980, 114800, 559650, 850668, (15312024+10073700+2066400)]
list2 = [1000000, 30000, 3000, 100, 50, 6, 6, 3, 2, 0]
list3 = [1000000, 90000, 9000, 300, 150, 18, 18, 9, 6, 0]

# Define the constant
constant = 29144841

# Ensure both lists are of the same length
if len(list1) != len(list2):
    print("Lists are not of the same length. Cannot compute product.")
else:
    # Calculate the intermediate product of the first list and the constant
    intermediate_product = [a/constant for a in list1]

    # Calculate the final product of the intermediate product and the second list
    Expected_Standard = [a*b for a, b in zip(intermediate_product, list2)]

    Expected_Sizzler = [a*b for a, b in zip(intermediate_product, list3)]

    # Prepare the data for the table
    table_data = list(zip(list1, intermediate_product, list2, Expected_Standard, list3, Expected_Sizzler))

    # Print the result in a table format
    print(tabulate(table_data, headers=["List1 Item", "Intermediate", "List2 Item", "Standard, List3 Item, Sizzler"]))
    # Print spacing
    print()

    print(sum(Expected_Standard), " Expected_Standard")
    print(sum(Expected_Sizzler), " Expected_Sizzler")
    print((sum(Expected_Sizzler))/2, " Expected_Sizzlerper dollar")