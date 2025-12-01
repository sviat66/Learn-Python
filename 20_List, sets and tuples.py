# collection =  single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "banana", "cherry", "mango"]
#print(dir(fruits))
#print(help(fruits))
# print(len(fruits))
# print("banana" in fruits)
# print(fruits.count("banana"))
# fruits[0] = "lemon" #we can change the list
# fruits.append("grape") #to add to the list
# fruits.remove("cherry")
# fruits.insert(2, "lime")
# fruits.sort()
# fruits.reverse()
# fruits.clear
# print(fruits.index("mango"))
# print(fruits.count("mango"))

# print(fruits[:2])
# for x in fruits:
#     print(x, end=" ")



# fruits = {"apple", "banana", "cherry", "mango"}
# print(fruits)
# fruits.add("lime")
# fruits.remove("apple")
# fruits.pop() #delete random object
# print(fruits)


fruits = ("apple", "banana", "cherry", "mango")
print("df" in fruits)
print(fruits.index("apple"))
fruits.count(("mango"))
print(fruits.count("mango"))


