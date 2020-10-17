t=int(input())
for i in range(t):
    n = int(input())
    d = dict()
    counter = 0 
    for j in range(n):
        value = 0
        s = input()
        if s in d:
            counter += d[s]//2
        else:
            value += 2
            for i in range(1,len(s)):
                if (s[i] == 'd' or s[i] == 'f') and (s[i-1] == 'f' or s[i-1] == 'd'):
                    value=value+4
                elif (s[i]=='j' or s[i]=='k') and (s[i-1]=='k' or s[i-1]=='j'):
                    value = value+4
                else:
                    value = value+2
            d[s] = value
            counter += value
    print(counter)