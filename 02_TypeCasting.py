#Typecasting =  the process of converting a variable form one data type to another
# str(), int(), float(), bool()

name = "Sviatoslav Oseredchuk"
age = 29
number = 5
gpa = 3.2
is_student = True

print(type(is_student))


age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

number += 1
print(number)

name = bool(name)
print (name)


