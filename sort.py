import math
n=1
while True:
	n=n+1
	if 8*n**2 <= 64*n*math.log2(n):
		pass
	else:
		print(n)
		break
	