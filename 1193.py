X = int(input())
n = 0
sum = (n * (n + 1)) % 2
while X > sum :
    sum = (n * (n + 1)) // 2
    n += 1
X = X - (n - 2) * (n - 1) // 2
if n % 2 == 1:
    s = '{0}/{1}'.format(X, n - X)
else :
    s = '{0}/{1}'.format(n - X, X) 
print(s)