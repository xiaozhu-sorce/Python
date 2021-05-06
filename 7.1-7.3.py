message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"Hello,{name}!")

age = input("How old are you?")
#此处的age接收的是str型21而不是int型
if int(age)>=18 :
	print("True")

#练习7-2
question=input("请问有多少人用餐？")
question=int(question)
if question >8:
    print("对不起，餐厅没有空桌。")
else:
    print("餐厅尚有余桌。")

#练习7-3
number = input("请输入一个数字")
number = int(number)
if number%10:
	print(f"\n{number}不是10的整数倍")
else:
	print(f"\n{number}是10的整数倍")
	
