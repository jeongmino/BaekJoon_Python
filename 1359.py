from math import factorial

N, M, K = map(int, input().split())

def makeMap(N, M, K):
    total = factorial(N - K) / ((factorial(M - K) ** 2) * factorial(N + K - (2 * M)))
    return int(total)

def makeReverseCase(N, M, K):
    sum = 0
    k = K - 1
    while k > 0:
        sum += makeMap(N, M, k)
        k -= 1
    if k == 0 and N >= 2 * M:
        sum += makeMap(N, M, k)
    return sum

totalNum = (factorial(N) / (factorial(N - M) * factorial(M))) ** 2            

prob = (totalNum - makeReverseCase(N, M, K)) / (totalNum / 2) * (factorial(N) / factorial(N - K) * factorial(K))

print(prob)          
