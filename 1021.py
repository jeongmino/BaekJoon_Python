from collections import deque
import sys 

def make_mid_num(num):
    mid_num = 0
    if num % 2 == 0:
        mid_num = num / 2 - 0.5 # 짝수개의 요소 중에 중앙값을 인위적으로 만듬. 인덱스로 활용할 변수기 때문에 0.5 - 1 = - 0.5 
    else:
        mid_num = num // 2 
    return mid_num

def shift_left(li):
    tmp = li[0]
    li.popleft()
    li.append(tmp)
    return 1

def shift_right(li):
    tmp = li[len(li) - 1]
    li.pop()
    li.appendleft(tmp)
    return 1
    
def pop_arg(li, arg): # li = 큐, arg = li_num[idx]
    median_var = make_mid_num(len(li))
    num_cnt = 0
    idx = li.index(arg)
    if idx <= median_var: # 이유는 뭔지 몰라도 idx = median_var 가 같을 때에는 shift_left가 더 빠르다....?
        while li[0] != arg:
            num_cnt += shift_left(li)           
    else:
        while li[0] != arg:
            num_cnt += shift_right(li)            
    li.popleft()
    return num_cnt
    
    
N, M = map(int, input().split())
queue = deque([])
for i in range(N, 0, -1):
    queue.appendleft(i)
    
li_num = list(map(int, sys.stdin.readline().split()))

cnt = 0 # 2, 3번의 횟수 
for i in li_num:
    cnt += pop_arg(queue, i)
print(cnt)
