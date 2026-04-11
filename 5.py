import math
n=int(input())
s=0
for number in range(1,n+1):
    s += int(math.sqrt(number)) # s=s+number
    print(s)