# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# # Expected output:

# # ["Mike", "Emma", "Kelly", "Brad"]

# def remove_emtpystr(list1):
#     return [x for x in list1 if x != ""]

# result = remove_emtpystr(list1
# print(result)

# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a/b
#     print("The answer of a divide by b:", c)
# except ValueError:
#     print("Entered value is wrong")
# except ZeroDivisionError:
#     print("Can't divide by zero")

# try:
#     a = int(input("Enter value of a:"))
#     b = int(input("Enter value of b:"))
#     c = a / b
#     print("The answer of a divide by b:", c)
# except(ValueError, ZeroDivisionError):
#     print("Please enter a valid value")

try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Can't divide with zero")
finally:
    print("Inside a finally block")