print("enter a number")
no=int(input())
ec=0
oc=0
while no!=0:
	r=no%10
	if no%2==0:
		ec=ec+1
	else:
		oc=oc+1
	no=no//10
print("no of even digit=",ec)
print("no of odd digit=",oc)
