# for loops = execute a block of code a fixed number of times.
#             You can iterate over a range, string, sequence, etc.

for x in range(1, 11):
    print(x)

for y in reversed(range(1, 11)):
    print(y)
print("Happy New Year")

for z in reversed(range(1, 11, 2)):
    print(z)
print("Happy New Year")

credit_card = "1234-5467-9010-3556"
for c in credit_card:
    print(c)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

