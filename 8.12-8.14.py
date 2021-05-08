def make_pizza(size,*toppings):
	"""打印顾客点的所有配料"""
	print("\nMaking a " + str(size) +"-inch pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)
		
make_pizza(16,'pepperoni')
make_pizza(12,'mushroons','green peppers','extra cheese')


def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('alnert','einstein',
							location='princeton',
							field='physics')
print(user_profile)

#练习8-12
def make_sanmingzhi(*toppings):
	print("\nMaking sanmingzhi whith the following toppings:")
	for topping in toppings:
		print("-" + topping)
		
make_sanmingzhi('cheese','vegetable','tomato')

#练习8-14

def car(c_shang,x_hao,**car_info):
	car_users ={}
	car_users['c_shang'] = c_shang
	car_users['x_hao'] = x_hao
	for key,value in car_info.items():
		car_users[key] = value
	return car_users
car_info = car('subaru', 'outback', color='blue', tow_package=True)
print(car_info)
