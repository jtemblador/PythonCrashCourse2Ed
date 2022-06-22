my_foods = ['pizza', 'falafel', 'carrot cake', 'hotdog', 'cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')


print(f"My favorite foods are {my_foods}.")
print(f"My friend's favoorite foods are {friend_foods}.")

print("The first three elements in the list: ")
for food in my_foods[:3]:
	print(food.title())

print("The middle three elements in the list: ")
for food in my_foods[1:4]:
	print(food.title())

print("The end three elements in the list: ")
for food in my_foods[-3:]:
	print(food.title())

