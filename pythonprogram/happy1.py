#wap to make range of happy number from 1 to 1000.
for no in range(1,1001,1):
	T=no 
	while T!=1 and T!=4:
		print(T)
		s=0
		while T>0:
			digit=T%10
			s=s+digit**2
			T=T//10
		T=s
	if T==1:
		print("no is a happy number")