#while loop = execute some code WHILE some conditions remains true
name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

food = input("Enter your food (q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")
print(f"Buy {name}")

num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"Num {num} is not between 1 and 10")
    num = int(input("Enter a number between 1 - 10: "))
print("Thats good")