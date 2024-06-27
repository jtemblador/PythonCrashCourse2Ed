orders = ['reuben', 'blt', 'burger']
fin_orders = []

while orders:
    order = orders.pop()
    print(f"Your {order} is ready!")

    fin_orders.append(order)

for order in fin_orders:
    print(f"A {order.title()} sandwich was made!")