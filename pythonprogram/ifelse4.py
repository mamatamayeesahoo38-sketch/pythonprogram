print("enter a number")
no=int(input())
if no<0:
	no=-no
if no<=9:
	print("no is single digit")
elif no<=99:
	print("no is double digit")
elif no<=999:
	print("no is triple digit")
else:
	print("other digit")