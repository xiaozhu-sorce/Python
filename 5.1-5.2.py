cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

banned_user = ['andrew','carolina','david']
user = 'marie'

if user not in banned_user:
	print(user.title()+",you can post a response if you wish")

car = 'subaru'
print("Is car == 'subaru'?I predict True.")
print(car=='subaru')

print("Is car == 'audi'?I predict False.")
print(car=='audi')
