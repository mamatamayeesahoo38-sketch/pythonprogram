print("enter a number")
no=int(input())
while no!=0:
	r=no%10
	no=no//10
print("first digit of number=",r)