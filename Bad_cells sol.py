the solution of bad cells 
quesion answer is in python 
a,b,x1,y1,x2,y2 = map(int,input().split())
s = abs((x1 + y1) // (2 * a) - (x2 + y2) // (2 * a))
s = max(s,abs((x1 - y1) // (2 * b) - (x2 - y2) // (2 * b)))
print(s)
