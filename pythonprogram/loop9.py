print("enter a number")
no=int(input())
c=0
while no!=0:
	no=no//10
	c=c+1
print("no of digit=",c)