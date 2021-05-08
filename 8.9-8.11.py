def greet_users(names):
	"""向列表中的美味用户发出简单的问候"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
		
usernames = ['hannah','ty','margot']
greet_users(usernames)


def print_models(unprinted_designs,completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model:{current_design}")
		completed_models.append(current_design)
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case','robot pendant','dodecahedron']
completed_models = []
#使用副本，使得unprinted_designs不会被清空
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)

#练习8-9,8-10
def show_magicians(magician_b):
    """显示魔术师"""
    for magician in magician_b:
        print(magician)

def make_great(magician_a,magician_b):
	"""了不起的魔术师"""
	while magician_a:
		mag = magician_a.pop()
		mag = 'the great ' + mag
		magician_b.append(mag)
    
m = ['魔术师1', '魔术师2', '魔术师3']
n = []
make_great(m[:],n)	
show_magicians(m)
show_magicians(n)
	
