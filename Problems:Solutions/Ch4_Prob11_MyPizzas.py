pizzas = ['pineapple', 'sausage', 'cheese']
friend_pizzas = pizzas[:]

pizzas.append('bacon')
friend_pizzas.append('pepperoni')

for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print()
for pizza in friend_pizzas:
	print(f"My friend likes {pizza} pizza.")

print("\nPizza is sooooooo good!")