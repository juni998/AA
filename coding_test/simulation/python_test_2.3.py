import sys
#sys.stdin=open("input.txt", "rt")

a=list(range(21))

for _ in range(10): # _(언더바) : 변수값 대입x
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0) # 0번 인덱스 삭제
for x in a:
    print(x, end=' ')