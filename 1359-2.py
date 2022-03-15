from math import factorial

N, M, K = map(int, input().split())

def makeMap(N, M, K):
    total = factorial(N - K) / ((factorial(M - K) ** 2) * factorial(N + K - (2 * M)))
    return int(total)

def makeReverseCase(N, M, K):
    sum = 0
    k = K
    while k <= M:
        sum += makeMap(N, M, k)
        k += 1
    return sum

totalNum = (factorial(N) / (factorial(N - M) * factorial(M))) ** 2     
prob = makeReverseCase(N, M, K) / totalNum       

print(prob)
print(totalNum)          
