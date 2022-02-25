T = int(input())
for i in range(T):
    N = int(input())
    li_x = []
    li_y = []
    for i in range(N):
        x, y = map(int, input().split())
        li_x.append(x)
        li_y.append(y)
    sort