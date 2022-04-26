import sys

T = int(input())
i = 1
while i <= T:
    li = list(map(int, sys.stdin.readline().split()))
    print('Case ' + '#' + '{0}: {1} + {2} = {3}'.format(i, li[0], li[1], li[0] + li[1]))
    i += 1