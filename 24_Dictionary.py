# dictionary = a collection of {key:values} pairs
#                 ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "Ukraine": "Kyiv",
            "UAE": "Abu Dhabi"}
print(capitals.get("UAE"))

capitals.update({"Germany": "Berlin"})

print(capitals)
# capitals.pop("Germany") #видалить ключ
# capitals.popitem() # видалить останній ключ
# print(capitals)
# capitals.clear()
# print(capitals) #Повністю видаляє

keys = capitals.keys() # виводить лише назву ключів
print(keys)
for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

items = capitals.items()
print(items)
for key, value in items:
    print(f"The capital of {key} is {value}.")



