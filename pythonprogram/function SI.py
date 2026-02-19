def sal():
	print("enter principle")
	P=int(input())
	print("enter time")
	T=int(input())
	print("enter rate of interest")
	R=int(input())
	SI=P*T*R/100
	print("simple interest=",SI)
	return
sal()