users = {}

if users:
	for user in users:
		if user == 'Admin':
			print("Admin privileges granted.")
		else:
			print(f"Welcome, {user}.")
else:
	print("Need more users!\n")

users = {'Ryan', 'Juan', 'Bob', 'Jack', 'Admin'}

if users:
	for user in users:
		if user == 'Admin':
			print("Admin privileges granted.")
		else:
			print(f"Welcome, {user}.")
else:
	print("Need more users!")
