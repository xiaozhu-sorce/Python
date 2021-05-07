def get_formatteed_name(first_name,last_name,middle_name=''):
	"""返回整洁的姓名"""
	#当中间名字为不为空的时候
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()
musician = get_formatteed_name('jimi','hendrix','Lee')
print(musician)
musician = get_formatteed_name('jimi','hendrix')
print(musician)


def build_person(first_name,last_name,age=None):
	person = {'first':first_name,'last':last_name}
	if age:
		person['age'] = age
	return person
	
musician = build_person('jimi','hendrix',age=27)
print(musician)

while True :
	print("\nPlease tell me your name:")
	print("(enter 'q' to at any time to quit)")
	f_name = input("First_name: ")
	if f_name =='q':
		break
	l_name = input("Last_name: ")
	if l_name =='q':
		break
	formatted_name = get_formatteed_name(f_name,l_name)
	print(f"\nHello,{formatted_name}!")

#8-7  8-8
def make_album(name, age, num):
    people = {'name': name, 'age': age, 'num': num}
    return people

while True:
    print("Please enter message: ")
    print("(enter 'q' at any time to quit)")
    name = input('name: ')
    if name == 'q':
        break
    age = input('age: ')
    if age == 'q':
        break
    num = input('num:')
    if num == 'q':
        break
    message = make_album(name, age, num)
    print(message)
