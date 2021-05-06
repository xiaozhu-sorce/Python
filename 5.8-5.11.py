request_toppings = ['mushroons','green peppers','extra cheese']
for request_topping in request_toppings:
	if request_topping == 'green peppers':
		print("Sorry,we are out of green peppers right now")
	else:
		print("Adding " + request_topping+".")
print("\nFinished making your pizza!")


request_toppings = []
if request_toppings: #当列表不为空时
	for request_topping in request_toppings:
		print("Adding " + request_topping+".")
	print("\nFinished making your pizza!")
else :
	print("Are you sure you want a plain pizza?")


available_toppings = ['mushroons','olives','green peppers','pepperoni','pineapple','extra cheese']
request_toppings = ['mushroons','french fries','extra cheese']
for request_topping in request_toppings:
	if request_topping in available_toppings:
		print("Adding " + request_topping+".")
	else : 
		print("Sorry,we don't have " + request_topping +".")
print("\nFinished making your pizza!")



current_users = ['mike','jone','alic','echo','dodo']
new_users = ['Mon','Tus','Jone','Echo','Bobo']
for new_user in new_users:
	if new_user.lower() in current_users :
		print("Please input other name!")
	else : 
		print("You can use this name!")
		


numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(str(number) + "st")
	elif number == 2:
		print(str(number) + "nd")
	elif number == 3:
		print(str(number) + "rd")
	else :
		print(str(number) + "th")
