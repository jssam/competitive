N,Q=map(int,input().split())
a=list(map(int,input().split()))

for i in range(Q):
    x=int(input())
    sum=0
    for i in range(0,N):
        if a[i]>=2*x:
           sum+=a[i]
        else:
            continue
            
    print(sum)
