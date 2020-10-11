m,r=[int(x) for x in input().split()]
mm=max(m,r)
low=min(m,r);
if(mm%low==0):
    print("Yes")
else:
    print("No")
