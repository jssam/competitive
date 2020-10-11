n,m,limn,f,L=10000,15000,int(10**13),int(input()),[]
 
def F(i):
	if i==0:
		return (0,1)
	a,b=F(i>>1)
	a,b=((2*a*b-a*a)%n,(b*b+a*a)%n)
	if i&1:
		a,b=(b%n,(a+b)%n)
	return (a,b)
 
for i in range(m):
	if F(i)[0]==f%n:
		L.append(i)
 
while n<limn:
	n*=10;
	T=[]
	for i in L:
		for j in range(10):
			if F(i+j*m)[0]==f%n:
				T.append(i+j*m)
	L=T;m*=10
	if L==[]:
		break
 
if L==[]:
	print(-1)
else:
	L.sort()
	print(L[0])
