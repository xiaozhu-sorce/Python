#在列表之间移动元素
unconfirmed_users = ['alice','brain','candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user:{current_user.title()}")
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#删除特定值的列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
	
print(pets)

#使用用户输入来填充字典
responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	#将name和response存储在字典中
	responses[name] = response
	
	repeat = input("Would you like to let another person respond?(yes/no) ")
	if repeat == 'no':
		polling_active = False
print("\n---Poll Result---")
for name,response in responses.items():
	print(f"{name} would like to climb {response}.")

#练习7-8
sandwich_orders=['Tuna sandwich','Ham cheese sandwich','Chicken sandwich']
finished_sandwiches=[]
while sandwich_orders:
    current_orders=sandwich_orders.pop()
    print("I made your "+current_orders.title()+".")
    finished_sandwiches.append(current_orders)
print("\nAll the sandwiches have been finished.")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

#练习7-9
sandwich_orders = ['pastrami', 'A', 'pastrami', 'B', 'pastrami', 'C']

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

#练习7-10
responses={}
active = True
while active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False

print("\n---  Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")
