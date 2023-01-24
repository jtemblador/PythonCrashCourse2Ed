users = {"albert", "LENNY", "pEtEr", "Cal"}
new_users = {"lenny", "PETER", "walter"}
usersCopy = {names.lower() for names in users}

if new_users:
	for user in new_users:
		if user.lower() in usersCopy:
			print(f"{user} is already taken!")
		else:
			print(f"{user} now created!")
