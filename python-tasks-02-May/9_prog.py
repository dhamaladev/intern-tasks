# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:

list1 = [5, 10, 15, 20, 25, 50, 20]
# Expected output:

# [5, 10, 15, 200, 25, 50, 20]

# def replace_item(list1, num):
#     index = list1.index(20)
#     list1[index] = num  
#     return list1

# result = replace_item(list1, 200)    
# print(result)
def replace_item(list1, given_num, num):
    for i in range(len(list1)):
        if list1[i] == given_num:
            list1[i] = num
            break
    return list1

result = replace_item(list1, 20, 200)    
print(result)