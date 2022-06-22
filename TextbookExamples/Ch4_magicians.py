magicians = ['alice', 'david', 'carolina']
for magician in magicians: #pulls name from list, associates it with variable magician.
	print(magician)

#It might help to read this code as “For every magician
#in the list of magicians, print the magician’s name.

for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thanks everyone, that was a great magic show!") 