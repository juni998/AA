import sys
#sys.stdin=open("input.txt", "rt")

t=int(input())
for t in range(t):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1: e]
    a.sort()
    print('#%d %d' %(t+1, a[k-1]))

