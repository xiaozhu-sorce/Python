alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")
print(alien_0['color'])
print(alien_0['points'])


print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25


alien_0 = {'x_position':0,'y_position':25,'speed':'medium',}
print(alien_0)
print("Original x-position:" + str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else : 
	#这个外星人的速度一定很快
	x_increment = 3
#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


#练习6-1
information = {
	'first_name' : 'Wu',
	'last_name' : 'kai',
	'age' : 19,
	'city' : 'lvliang' ,	
	}
print (information)
favorite_number = {
	'Zhukemeng' : 7,
	'Lixiang' : 8,
	'Leigangjian' : 3,
	'Wukai' : 2,
	'Fengshidan' : 7,
	}
print(favorite_number)
