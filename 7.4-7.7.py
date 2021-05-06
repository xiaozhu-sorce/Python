current_number = 0
while current_number < 10:
	current_number+=1
	if current_number % 2 == 0:
		continue
	
	print(current_number)
	

prompt = "\nTell me somrthing,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt+="\nEnter 'quit' to end the program."
while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

#练习7-4
shuru = "请输入你需要添加的pizza配料："
shuru +="\n当你输入quit，将停止添加配料："
pizzas = ""
while pizzas != 'quit':
    pizzas = input(shuru)
    if pizzas != 'quit':
        print("你的比萨添加"+pizzas+"成功\n")
        
#练习7-5
prompt = "\nPlease enter you age:"
prompt+="\nEnter 'quit' to end the program."
while True :
	age = input(prompt)
	if age == 'quit':
		break
	else : 
		age = int(age)
		if age < 3:
			print("免费")
		elif age < 12:
			print("需要10美元")
		else :
			print("需要15美元")

#练习7-6
while 1:
	print("1")
	
