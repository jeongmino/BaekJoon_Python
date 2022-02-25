def makeNewLi(li_arg, N, K):
    li_ret = []
    i = 0
    cnt = K
    breakPoint = N
    while True:
        if len(li_ret) == breakPoint:
            break
        if cnt == 0:
            li_ret.append(str(li_arg[i]))
            del li_arg[i]
            cnt = K
            N -= 1
        else:
            i += 1
            cnt -= 1
        if i == N:
            i = 0
    return li_ret
                  
N, K = map(int, input().split())
K -= 1 ## 함수 인자로 전하지 않기 위해 + 인덱스처럼 사용
li_input =[]
for i in range(1, N + 1):
    li_input.append(i)
li = makeNewLi(li_input, N, K)
print("<" + ", ".join(li) + ">")