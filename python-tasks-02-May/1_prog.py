import math
list1 = [100, 200, 300, 400, 500]
# Expected output:

# [500, 400, 300, 200, 100]

def reverse_list(list1):
    for i in range(math.floor(len(list1)/2)):
          list1[i], list1[len(list1) - 1 - i] = list1[len(list1) - 1 - i],list1[i]
    return list1      

result = reverse_list(list1)    
print(result)
