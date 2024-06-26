
budget = input("What's you budget on a new car? ")
budget = int(budget)

if budget > 100000:
    print(f"With {budget}, you could buy a Porsche!")
elif budget > 80000:
    print(f"With {budget}, you could buy a Hellcat!")
elif budget > 50000:
    print(f"With {budget}, you could buy a Mercedes")
elif budget > 30000:
    print(f"With {budget}, you could buy a Honda!")
elif budget > 10000:
    print(f"With {budget}, you could buy a Nissan!")


