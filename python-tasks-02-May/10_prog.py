# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output:

# [5, 15, 25, 50]

def remove_occurences(list):
    return [x for x in list if x != 20]

result = remove_occurences(list1)
print(result)
