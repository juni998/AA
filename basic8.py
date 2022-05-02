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

