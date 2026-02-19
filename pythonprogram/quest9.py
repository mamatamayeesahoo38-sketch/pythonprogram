#find the SI using function return with argument
def sal(p,t,r):
	SI=p*t*r/100
	return SI
print("enter principal")
p=int(input())
print("enter time")
t=int(input())
print("enter rate of interest")
r=int(input())
res=sal(p,t,r)
print("simple interest=",res)