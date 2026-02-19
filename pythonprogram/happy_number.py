print("enter a number")
n=int(input())
T=n
while T!=1 and T!=4:
	s=0
	while T>0:
		d=T%10
		s=s+d*d
		T=T//10
	T=s
if T==1:
	print(n,"is happy number")
else:
	print(n,"is not a happy number")