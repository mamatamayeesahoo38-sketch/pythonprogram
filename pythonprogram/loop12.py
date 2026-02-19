print("enter a number")
no=int(input())
es=0
os=0
while no!=0:
	r=no%10
	if no%2==0:
		es=es+r
	else:
		os=os+r
	no=no//10
print("sum of even digit=",es)
print("sum of odd digit=",os)
