#리스트와 내장함수

a=[23, 12, 36, 53, 19]
print(a[:3]) #0~2번 인덱스 출력
print(a[1:4]) #1~3번 인덱스 출력
print(len(a)) #리스트 길이 출력

for i in range(len(a)):
    print(a[i], end=' ') #리스트 출력1
print()

for x in a:
    print(x, end=' ') #리스트 출력2
print()

for x in enumerate(a): #튜플 형태로 출력
    print(x)           #(0, n[0])(1, n[1]) ~~

b=(1, 2, 3, 4, 5) # 튜플
print(b[0])
#b[0] = 7: 튜플은 변경x

for x in enumerate(a):
    print(x[0], x[1]) #출력
print()

for index, value in enumerate(a): # index: 0, value: 23
    print(index, value)
print()

if all(20>x for x in a): # 60>x 비교 x=23, 12, 36, 53, 19
    print("YES")         # 모두가 참 or 거짓일때
else:
    print("NO")

if any(15>x for x in a): # any: 한번이라도 참이면 참, 모두가 거짓일때 거짓
    print("YES")
else:
    print("NO")

