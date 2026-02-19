a=25
def show():
	a=30
	print(a)
	print(locals()['a'])
	print(globals()['a'])
	globals()['a']=50
show()
print(a)
