def display_message(main):
    print(f"{main}")
    msg = input("Name: ")
    age = input("Age: ")
    age = int(age)

    print(f"Hello, {msg.title()}!")
    print(f"You're {age}")

display_message("Hello From Main!")