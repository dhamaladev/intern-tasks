# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:

numbers = [1, 2, 3, 4, 5, 1.6]
# Expected output:

# [1, 4, 9, 16, 25, 36, 49]

def square_list(numbers):
    for x in numbers:
         valid_numbers = [x for x in numbers if isinstance(x, int) or isinstance(x, float)]
    return [x*x for x in valid_numbers]

result = square_list(numbers)
print(result)
