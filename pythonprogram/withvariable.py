"""
1
2 3 
4 5 6
 7 8 9 10
c=0
for i in range (1,5,1):
	for j in range (1,i+1,1):
		c=c+1
		print(c,end="\t")
	print()