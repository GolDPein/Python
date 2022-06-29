import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
print(sys.getrecursionlimit())

N = 3000

def sumTillN(n):
    if n == 1: return 1
    return n + sumTillN(n-1)

print(sumTillN(N))
