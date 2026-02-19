print("enter two number")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult\n4.div")
ch=int(input())
if ch==1:
	print("sum=",no1+no2)
elif ch==2:
	print("substract=",no1-no2)
elif ch==3:
	print("multiply=",no1*no2)
elif ch==4:
	print("divide=",no1%no2)
else:
	print("invalid choice")