"""
1
2 3
4 5 6
7 8 9 10
#n*(n+1)/2
j=1
for i in range(1,5):
	while j<=i*(i+1)/2:
		print(j,end="\t")
		j=j+1
	print()