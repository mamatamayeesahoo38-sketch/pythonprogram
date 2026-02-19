#wap to make range of happy number.
n=13
T=n
while T!=1 and T!=4:
	print("Hi ",T)	
	s=0
	while T>0:
		digit=T%10
		s=s+digit**2
		T=T//10
	T=s
if T==1:
	print(n,"is a happy number")