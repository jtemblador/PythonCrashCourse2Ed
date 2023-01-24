requested_topppings = ['mushrooms', 'extra cheese', "green peppers"]

if 'mushrooms' in requested_topppings:
	print("Adding mushrooms")

if 'pepperoni' in requested_topppings:
	print("Adding pepperoni")

if 'extra cheese' in requested_topppings:
	print("Adding extra cheese")


print("Finished making your pizza!\n")


for requested_toppping in requested_topppings:
	if requested_toppping == 'green peppers':
		print("Sorry all out of green peppers")
	else:
		print(f"Adding {requested_toppping}.")

print("Finished making your pizza!\n")

requested_topppings = {}
if requested_topppings:
	for requested_toppping in requested_topppings:
		print(f"Adding {requested_toppping}")
	print("Finished making your pizza\n")
else:
	print("Are you sure you want a plain pizza?\n")



available_toppings = {'mushrooms', 'olives', 'green peppers', 
					  'pepperoni', 'pineapple', 'extra cheese'}
requested_topppings = {'mushrooms', 'french fries', 'extra cheese'}

for topping in requested_topppings:
	if topping in available_toppings:
		print(f"Adding {topping}.")
	else:
		print(f"We don't have {topping}.")
