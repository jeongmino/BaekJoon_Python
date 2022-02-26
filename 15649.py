
N, M = map(int, input().split())
li = []
for i in range(1, N+1):
    li.append(i)
start_answer = ""
def recursiveP(li_input, answer): 
    if N - M == len(li_input):
        print(answer)
    else:
        for num in li_input:
            copyList = li_input.copy()
            copyList.remove(num)
            new_answer = answer + f"{num} "
            recursiveP(copyList, new_answer)

recursiveP(li, start_answer)
            
        