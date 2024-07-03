players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #printing a slice of list 
print(players[1:4])	#printing a slice of list 
print(players[:4])	#if no start, will begin from beginning 
print(players[4:])	#if no end, will go to end 
print(players[-3:])	#prints last 3 elements of list

for player in players[-3:-1]: # prints from third to last all the way to 
	print(player.title())
