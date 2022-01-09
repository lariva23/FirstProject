line=5
a=2*line-1
b=1
for i in range(0,2*line-1):
	for j in range(1,b):
		print(' ' , end="")
	for k in range(0,a):
		print('*',end="")
	a=a-2
	b=b+1
	print("\n")


