
N, num = map(int, input().split())
li_input = []
li_ret = []
for n in range(1, N + 1):
    li_input.append(n)
K = num - 1
num -= 1 
i = 0
N -= 1 ## N 을 index에 맞춤
print(li_input)
while True:
    if num == 0:
        li_ret.append(li_input[i])
        del li_input[i]
        N -= 1 
        num = K
        i -= 1     
    i += 1
    num -= 1
    if  i == N:
        i = 0
    if len(li_input) == 0:
        break
print(li_ret)

