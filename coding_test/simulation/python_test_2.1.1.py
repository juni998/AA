import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    if s==s[::-1]: # s[::-1] == s의 reverse
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
