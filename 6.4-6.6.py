user_0 = {
	'user_name' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi'
	}
#items()返回一个键值对列表
for key,value in user_0.items():
	print("\nKey:" + key)
	print("Value:" + value)
	
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}	
#keys()只遍历 键 或者默认遍历键
for name in favorite_languages.keys():
	print(name.title())
#按照顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for talking the poll.")
#按照顺序遍历字典中的所有值  使用set()来剔除重复项
for name in set(favorite_languages.values()):
	print(name.title())
