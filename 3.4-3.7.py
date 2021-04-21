name_list=['mother','father','grandfather','grandmother']
print(name_list)
leave=name_list.pop(2)
print(leave+"  can't attend this party")
name_list.append('uncle')
print(name_list)
print("find a big table")
name_list.insert(0,'aunt')
name_list.insert(2,'brother')
print(name_list)
print("There are only two people can attend this party")
leave=name_list.pop(5)
print("Sorry! "+leave)
leave=name_list.pop(4)
print("Sorry! "+leave)
leave=name_list.pop(3)
print("Sorry! "+leave)
leave=name_list.pop(2)
print("Sorry! "+leave)
leave=name_list[1]
print("Come！ "+leave)
leave=name_list[0]
print("Come! "+leave)
print(name_list)
del name_list[1]
del name_list[0]
print(name_list)
