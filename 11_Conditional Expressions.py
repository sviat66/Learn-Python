# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition els
from os import access

num = 7
a = 6
b = 7
age = 2
temperature = 5
user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
max_num =  a if a > b else b
min_num =  a if a < b else b
status = "Adult" if age >=18 else "Child"
weather = "Its hot outside" if temperature >= 25 else "Its cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(max_num)
print(min_num)
print(status)
print(weather)
print(access_level)