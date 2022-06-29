import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

N = 3000
nSum = N * (N+1) // 2
print(nSum)

def sumTillN(n):
    if n == 1: return 1
    return n + sumTillN(n-1)

print(sumTillN(N))
