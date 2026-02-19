#Take a employee salary from keyboard sal=5000,da=30, hra=20 if sal<5000,da==10,hra==5 display basic sal,dahra total sal
print("basic sal")
sal=float(input())
da,hra=0,5000
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",totalsal)
