
from collections import Counter
import math

def getDivisorsLen(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
            if (n / i == i) : 
                cnt = cnt + 1
            else :
                cnt = cnt + 2
                  
    return cnt 

def isPrime(n): 
    if n <= 1: 
        return False
  
    for i in range(2,n): 
        if n % i == 0: 
            return False

    return True

def noOfOccurences(n):
    count = dict(Counter(str(n)))
    values = list(count.values())

    if( len(set(values)) == 1):
        return True
    else:
        return False
    


no_of_testcase = int(input())

for i in range(no_of_testcase):
    inp = int(input())
    D = getDivisorsLen(inp)

    if noOfOccurences(inp) == False:
        if isPrime(D) == False:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
