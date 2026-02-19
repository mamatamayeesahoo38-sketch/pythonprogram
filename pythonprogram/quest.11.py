#find the area of rectangle using funtion return value with no argument
def area():
	print("enter length of rect")
	l=int(input())
	print("enter breadth of rect")
	b=int(input())
	a=l*b
	return a
res=area()
print("area=",res)