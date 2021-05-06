players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3] :
	print(player.title())
	
print("Here are the middle three players on my team:")
for player in players[2:5] :
	print(player.title())

print("Here are the last three players on my team:")
for player in players[-3:] :
	print(player.title())
	
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("my favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are :")
print(friend_foods)

for food in my_foods[:]:
	print(food)
