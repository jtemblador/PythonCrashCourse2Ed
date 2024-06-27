prompt = "Enter a pizza topping: "
flag = True

while flag:
    topping = input(prompt)
    if topping != 'quit':
        print(topping.title())
    else:
        break
    