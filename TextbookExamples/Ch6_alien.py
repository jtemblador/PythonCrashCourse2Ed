
#Create empty dictionary with brackets
alien_0 = {}

#Add elements key = value
alien_0['color'] = 'green'
alien_0['points'] = 5


print(alien_0)

alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

print(alien_0)

print(f"The alien is {alien_0['color']}.")
#Change alien color
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

alien_0['speed'] = 'medium'

print(f"Original alien position: {alien_0['x_pos']}")
#Changing x_pos
if alien_0['speed'] == 'slow' :
    x_increment = 1
elif alien_0['speed'] == 'medium' :
    x_increment = 2
else:
    x_increment =3

#Creating the new position of x_pos    
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

#printing x_pos
print(f"New alien position is: {alien_0['x_pos']}")
    
#Deleting a key in a dictionary
print(f"Original points is: {alien_0['points']}")
del alien_0['points']
print(f"Points deleted, {alien_0}")

#Getting the default value from a dictionary
# .get will return the value if it exists or return the text if it doesn't exist 
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


