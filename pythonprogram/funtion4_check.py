def check(no):
	if no%2==0:
		return "no is even"
	else:
		return "no is odd"
	return
print("enter a number")
no=int(input())
res=check(no)
print("no=",res)
