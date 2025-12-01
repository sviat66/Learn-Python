# name = input("Enter your full name: ")
# # result = len(name)
# # result = name.find("a")
# # result2 = name.rfind("a")
# # name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# print(result)
# # print(result2)
# print(name)

# phone_number = input("Enter your phone number: ")
# # result = phone_number.count("-")
# result = phone_number.replace("-", " ")
# print(result)
# print(help(str))

# Exercise Validate user input
# 1  Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must not contain digits

user_name = input("Please enter user name: ")
name_len = len(user_name)
name_space = user_name.count(" ")
name_digit = any(char.isdigit() for char in user_name)
# print(name_digit)
# print(name_len)
# print(name_space)
# if len(user_name) > 12:
#     print("User Name too long")
# elif not user_name.find(" ") == -1:
#     print("User Name can't contain spaces")
# elif not user_name.isalpha():
#     print("User Name can't contain digits")
# else:
#     print("hello")

erros = False

if len(user_name) > 12:
    print("User Name is too long (max 12 characters)")
    erros = True

if " " in user_name:
    print("User Name can't contain spaces")
    erros = True

if any(char.isdigit() for char in user_name):
    print("User Name can't contain digits")
    erros = True

if  not erros:
    print("You are good to go ✅")

# if name_len > 12 and name_space == 0 and not name_digit:
#     print("User Name is too long")
# elif name_len > 12 and name_space > 0 and not name_digit:
#     print("User Name is too long")
#     print("User Name cant contain spaces")
# elif name_len > 12 and name_space > 0 and  name_digit:
#     print("User Name is too long")
#     print("User Name cant contain spaces")
#     print("User Name cant contain digits")
# elif name_space > 0 and name_digit:
#     print("User Name cant contain spaces")
#     print("User Name cant contain digits")
# elif name_digit:
#     print("User Name cant contain digits")
# elif name_digit and name_len > 12:
#     print("User Name cant contain digits")
#     print("User Name is too long")
# elif name_space > 0:
#     print("User Name cant contain spaces")
# elif name_space > 0 and name_digit:
#     print("User Name cant contain spaces")
#     print("User Name cant contain digits")
# else:
#     print("You are good to go")


