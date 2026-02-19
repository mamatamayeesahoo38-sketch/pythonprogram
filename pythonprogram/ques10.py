#check no even odd using function no return value no argument
def no():
	print("enter a number")
	no=int(input())
	if no%2==0:
		print("no is even")
	else:
		print("no is odd")
	return
no()