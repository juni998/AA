import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
max = -214000000

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)

    return sum

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x

print(res)



