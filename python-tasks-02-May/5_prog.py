# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# Expected output:


# 10 400
# 20 300
# 30 200
# 40 100

def iterate_lists(list1, list2):
    new_list = zip(list1, reversed(list2))
    return new_list

result = iterate_lists(list1, list2)    
for x,y in result:
    print(x,y)