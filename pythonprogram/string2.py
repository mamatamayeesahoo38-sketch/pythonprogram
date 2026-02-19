print("enter a string")
s=input()
alp,lw,up,vw,co,dg,sp,wd,v,sy=0,0,0,0,0,0,0,0,0,0
for i in s:
	c+=1
	if i.isalpha():
		alp+=1
		if i.isupper():
			up+=1
		else:
			lw+=1
		if i in "aeiouAEIOU":
			vw+=1
		else:
			co+=1
	elif i.isdigit():
		dg+=1
	elif i.isspace():
		sp+=1
	else:
		sy+=1
	c=c+1
print("total no of char=",c)
print("total no of alp=",alp)
print("total no of vw=",vw)
print("total no of co=",co)
print("total no of upper=",up)
print("total no of lower=",lw)
print("total no of digit=",dg)
print("total no of space=",sp)
print("total no of sy=",sy)
print("total no of word=",wd)