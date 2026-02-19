print("enter a number")
no=int(input())
ec=0
oc=0
es=0
os=0
while no!=0:
	r=no%10
	if no%2==0:
		ec=ec+1
		es=es+r
	else:
		oc=oc+1
		os=os+r
	no=no//10
print("no of even digit=",ec)
print("no of odd digit=",oc)
print("sum of even digit=",es)
print("sum of odd digit=",os)
