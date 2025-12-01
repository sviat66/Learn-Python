#nested loop = A loop within another loop (outer, inner)
#              outer loop:
#                    inner loop:

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use: ")

for y in range(rows):
    for x in range (columns):
        print(symbol, end="")
    print()
