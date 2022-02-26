N, M = map(int, input().split())
start_list = []
for i in range(1, N + 1):
    start_list.append(i)
start_answer = ""

def next(answer, input_list):
    
    if len(input_list) == N - M:
        print(answer)
    else:
        for num in input_list:
            copied_list = input_list.copy()
            copied_list.remove(num)
            renew_answer = answer + f" {num}"
            next(renew_answer, copied_list)
        
next(start_answer, start_list)


