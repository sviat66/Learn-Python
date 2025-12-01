# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    # print("Principle can`t be less than or qual to zero")
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can`t be less than or qual to zero")

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can`t be less than or qual to zero")
    else:
        break

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("rate can`t be less than or qual to zero")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("time can`t be less than or qual to zero")

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} years: ${total:.2f}")
