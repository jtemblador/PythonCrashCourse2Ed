#Using f string
first_name = "ada"
last_name  = "lovelace"
full_name  = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Using \t
message = f"Hello, \t{full_name.title()}!"
print(message)

#Using \n 
message = f"Hello, \n{full_name.title()}!"
print(message)