import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
res = list(map(int, input().split()))
tot = 0
sum = 0


for i in range(n):
    if res[i] == 1:
        tot += 1
        sum += tot
    else:
        tot = 0

print(sum)
