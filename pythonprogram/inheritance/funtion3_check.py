def check():
	print("enter a number ")
	no=int(input())
	if no%2==0:
		return "even number"
	else:
		return "odd number"
res=check()
print(res)