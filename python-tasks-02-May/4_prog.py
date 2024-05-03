# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take", "nsfosd", 1]
list2 = ["Dear", "Sir", "wojeiwerwe", "we9w98erwe"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate_lists(list1, list2):
    new_list = []
    for i in range(len(list1)):
      if not isinstance(list1[i], str):
         list1[i] = str(list1[i])
      for j in range(len(list2)):
        if not isinstance(list2[j], str):
         list2[j] = str(list2[j])
        new_list.append(list1[i]+" "+list2[j])
    return new_list   

result = concatenate_lists(list1, list2)
print(result)
