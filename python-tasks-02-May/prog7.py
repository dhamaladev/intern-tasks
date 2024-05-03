# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def insert_one(list1, num):
    for x in range(len(list1)):
        if isinstance(list1[x], list):
            for i in range(len(list1[x])):
                if isinstance (list1[i], list):
                    for z in list1[i]:
                        if isinstance (z, list):
                            z.append(num)
    return list1    

result = insert_one(list1, 7000)
print(result)