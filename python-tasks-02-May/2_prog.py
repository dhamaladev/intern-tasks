# Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

# list1 = ["M", "na", "i", "Ke", 1, 6]
# list2 = ["y"]
list1 = []
list2 = []
# Expected output:

# ['My', 'name', 'is', 'Kelly']
def check_type(lst):
    for i in range(len(lst)):
        if not isinstance(lst[i], str):
            lst[i] = str(lst[i])
    return lst

def concatenate_lists(list1, list2):
    list1 = check_type(list1)
    list2 = check_type(list2)
    result = []
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        result.append(list1[i] + list2[i])
    if len(list1) > len(list2):
        result.extend(list1[min_length:])
    elif len(list2) > len(list1):
        result.extend(list2[min_length:])
    return result

# Given lists
# list1 = ["M", "na", "i", "Ke", 1]
# list2 = ["y"]

# Concatenate lists index-wise
result = concatenate_lists(list1, list2)
print(result)

