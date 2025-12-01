#indexing = accesing elements of sequence using [] (indexing operators)
# [stat : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[5])
print(credit_number[0:4])
print(credit_number[-2])
print(credit_number[::2])#every second carachcer

last_digits = credit_number[-4:]
print(last_digits)
reversed_number = credit_number[::-1]
print(reversed_number)
