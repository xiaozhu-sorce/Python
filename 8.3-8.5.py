#默认参数只能放在后面
def describe_pet(pet_name,animal_type='dog'):
	"""显示宠物的信息"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry')
describe_pet(pet_name = 'willie',animal_type = 'cat')
