for i in range (1,5,1):
	for j in range (1,i+1,1):
		print(j,end="\t")
	for j in range(i,0,-1):
		print(j,end="\t")
	print()
for i in range (4,0,-1):
	for j in range (1,i+1,1):
		print(j,end="\t")
	for j in range (i,0,-1):
		print(j,end="\t")
	print()