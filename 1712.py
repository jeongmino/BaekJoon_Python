A,B,C = map(int, input().split())
n = 1
if C <= B :
    print (-1)
else:
    n = A // (C - B) + 1
    print(n)