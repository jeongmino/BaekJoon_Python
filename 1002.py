import sys
import math
T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split(" "))
    if x1 == x2 and y1 == y2 and r1 == r2 :
        print(-1)
    else:
        d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) 
        if d < r1 + r2 and r2 < d + r1 and r1 < d + r2:
            print(2)
        elif d == r1 + r2 or r1 == d + r2 or r2 == d + r1:
            print(1)
        else:
            print(0)
