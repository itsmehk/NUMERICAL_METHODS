h=0.2

def function(x,y):
	return -2*y*y*x

def X(n):
	if n==0 :
	
		return 0
	
	else :
		return X(n-1)+h

def Y(n):
	if n==0 :
		return 1
	else :
		return Y(n-1) +h*function(X(n-1),Y(n-1))

n=5
while n>=0:
	print "Y(" + str(h*n) + ") :" + str(Y(n))
	n=n-1

