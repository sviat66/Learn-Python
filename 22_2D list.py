# fruits = ["apple", "mango", "banana"]
# vegetables = ["celery", "carrats", "potatoes"]
# meats = ["chiken", "fish", "turkey"]
#
# groceries = [fruits, vegetables, meats]#or copy entire row here , just separate them with coma
#
# # print(groceries)
# # print(groceries[0])
# # print(groceries[1])
# # print(groceries[0][1])
#
# for collection in groceries:
#     # print(collection)
#     for item in collection:
#         print(item, end=" ")
#     print()

num_pad = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"), ("*", "0", "#"))
for num in num_pad:
    for char in num:
        print(char, end=" ")
    print()