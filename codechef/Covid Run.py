t = int(input())
for i in range(t):
    n, k, x, y = list(map(int, input().split(" ")))
    arr1 = ["0"]*n
    while arr1[x] != '1':
        arr1[x] = '1'
        x = (x+k)%n
        
    if arr1[y] == '0':
        print("NO")
    else:
        print("YES")