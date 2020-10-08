n=int(input())
a=[0]
b=[int(x) for x in input().split()]
a=a+b
m=int(input())
for i in range(m):
    x,y=[int(x) for x in input().split()]
    if((x-1)>=1):
        a[x-1]+=(y-1)
    if((x+1)<=n):
        a[x+1]+=(a[x]-y)
    a[x]=0
for i in range(1,n+1):
    print(a[i],end=" ")
