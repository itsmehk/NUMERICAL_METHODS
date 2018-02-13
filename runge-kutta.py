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
		K1=h*function(X(n-1),Y(n-1))
		K2=h*function(X(n-1	)+h/2,Y(n-1)+K1/2)
		K3=h*function(X(n-1)+h/2,Y(n-1)+K2/2)
		K4=h*function(X(n-1)+h,Y(n-1)+K3)
		return Y(n-1)+(1/6)*(K1 + 2*K2 + 2*K3 + K4)

n=5
while n>=0:
	print "Y(" + str(h*n) + ") :" + str(Y(n))
	n=n-1