"""
1 1 
1 2 2 1
1 2 3 3 2 1
1 2 3 4 4 3 2 1
for i in range (1,5,1):
	for j in range (1,i+1,1):
		print(j,end="\t")
	for j in range (i,0,-1):
		print(j,end="\t")
	print()