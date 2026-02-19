import sys
print("enter a char")
ch=input()
if len(ch)!=1:
	print("single char allow")
	sys.exit()
print(ch)
print(ord(ch))