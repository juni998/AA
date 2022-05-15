import sys
#sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
ave = (sum(a)/n)+0.5
ave = int(ave)
'''
파이썬의 round: round_half_even 방식
#파이썬의 반올림 방법:
a=66.6
a=a+0.5
a=int(a)
'''
min = 214000000

for idx, x in enumerate(a):
    tmp=abs(ave-x)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)