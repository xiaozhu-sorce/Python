alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
#在列表中存储字典
#列表中的每一个元素都是字典
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
	print(alien)

#这是一个存储外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)
#改变前三个外星人的数据
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print("```")
#显示创建了多少外星人  注意f
print(f"Total number of aliens:{len(aliens)}")


#存储所点比萨的信息
#在字典中存储列表 在字典中的键对应的值是一个列表
pizza = {
	'crust':'thick',
	'toppings':['mushroons','extra cheese']
	}
print(f"You ordered a {pizza['crust']}-crust pizza"
	" with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)


favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
	}
#用循环输出字典中的值列表
for name,languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")


#在字典中存储字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		},
	}
for username,user_info in users.items():
	print(f"\nUsername:{username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	
	print(f"\tFull name:{full_name.title()}")
	print(f"\tLocation{location.title()}")
