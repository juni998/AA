import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s) #문자열의 길이
    for j in range(size // 2):
        #파이썬은 인덱스 거꾸로 접근 가능
        if s[j] != s[-1-j]: #0번 인덱스와 마지막 인덱스 비교
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

