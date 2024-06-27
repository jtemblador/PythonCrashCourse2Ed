orders = ['reuben', 'pastrami', 'blt', 'pastrami', 'burger', 'pastrami',]
fin_orders = []
print("We've run out pastrami!\n")

# removing pastrami from list
while 'pastrami' in orders:
    orders.remove('pastrami')
    print("Pastrami removed from list!")

# getting ordewrs ready
while orders:
    order = orders.pop()
    print(f"Your {order} is ready!")

    fin_orders.append(order)

# orders made
for order in fin_orders:
    print(f"A {order.title()} sandwich was made!")
    
