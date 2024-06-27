prompt = "What is your age? "

age = input(prompt)
age = int(age)

if age > 12:
    print("Ticket price: $15")
elif age > 3:
    print("Ticket price: $10")
else:
    print("You're too young to go to the movies!")