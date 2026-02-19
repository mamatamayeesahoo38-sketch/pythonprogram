#take a number from keyboard find the sum of digit
print("enter a number")
no=int(input())
s=0
while no!=0:
	r=no%10
	s=s+r
	no=no//10
print("sum of digit=",s)