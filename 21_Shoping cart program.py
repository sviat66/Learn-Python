# Shpoing car program

foods = []
prices = []
total = 0

while True:
     food = input("Enter a food to buy (q to quit): ")
     if food.lower() == "q":
         break
     else:
         price = float(input(f"Enter the price of {food}: $"))
         foods.append(food)
         prices.append(price)

print("---- YOUR CART ----")

for food, price in zip(foods, prices):
    print(f"{food} ---- ${price}")

for price in prices:
    total = total + price

print(f"Total price is ${total:.2f}")
