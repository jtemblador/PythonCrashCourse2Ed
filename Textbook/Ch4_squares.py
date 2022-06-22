squares = []

for val in range(1, 11):	#Finds the square of nums 1-10
	square = val ** 2
	squares.append(square)
print(squares)

#Can also do all in one line 

squares = []

for val in range(1, 11):
	squares.append(val ** 2)	#all in one line
print (squares)

squares = []
squares = [val ** 2 for val in range(1, 11)]
print (squares)