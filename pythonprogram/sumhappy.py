#wap sum of first 10 happy number
c=0
s=0
for no in range(1,1000):
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
		print(n,"is a happy number")
		s=s+n
		c=c+1
	if c==10:
		break
		print("sum of first 10 happy number=",s)
