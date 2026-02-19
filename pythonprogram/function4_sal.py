def sal(p,t,r):
	sal=p*t*r/100
	return sal
print("enter principle")
p=int(input())
print("enter time")
t=int(input())
print("enter rate of interest")
r=int(input())
res=sal(p,t,r)
print("sal=",res)