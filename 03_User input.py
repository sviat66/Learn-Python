# input () = A function that promts the user to enter data
# Returns the entered data as a string

name = input("What is your name?:")
age = int(input("How old are you?:"))

# age = int(age)
age = age + 1

print(f"Hello {name}")
print("Happy Birthday")
print(f"You are {age} years old")

#Exercise 1 Rectangle Area Calc
width = int(input("Enter the width of Rectangle:")) #or can be float
length = int(input("Enter the length of Rectangle:"))
area = width * length
print(f"Area of Rectangle is {area}cm²") # alt+0178 on numpad

#Exercise 2 Shopping Cart Program
item = input("What item would you like to buy:")
price = float(input("Enter the price of item:"))
quantity = int(input("How many would you like?:"))
total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")
