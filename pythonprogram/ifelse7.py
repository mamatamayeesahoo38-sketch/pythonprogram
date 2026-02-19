print("enter a number divisible by 5")
no=int(input())
if no%5==0 and no%7==0:
	print("no is diviosible by of 5 and 7")
elif no%5==0:
	print("no is multiple of 5")
elif no%7==0:
	print("no is divisible by 7")
else:
	print("no is invalid")