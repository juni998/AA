#리스트와 내장함수
import random as r

#리스트 선언법
from audioop import reverse

b=list()
print(b)

a=[1, 2, 3, 4, 5]
print(a)
print(a[0]) #0번 인덱스 출력

b=list(range(1, 11)) #1~10까지 리스트에 입력
print(b)

c=a+b #a리스트, b리스트 합치기
print(c)

print(a)
a.append(6) #a리스트에 6추가
print(a)

a.insert(3, 7) #3번 인덱스에 7추가
print(a)

a.pop() #마지막 인덱스 제거
print(a)

a.pop(3) #3번 인덱스 제거
print(a)

a.remove(4) #리스트 내 숫자4 삭제
print(a)

print(a.index(5)) #리스트 내 숫자5의 인덱스 번호 출력

a=list(range(1,11))
print(a)
print(sum(a)) #리스트 내 모든 값 합 출력
print(max(a)) #리스트 내 제일 큰 값 출력
print(min(a)) #리스트 내 제일 작은 값 출력
print(min(7, 5)) # 7과 5중에 최소값 출력
print(a)

r.shuffle(a) #랜덤함수의 shuffle: 모든 값 섞기
print('내림차순: ')
a.sort(reverse=True) #내림차순 정렬
print(a)
a.sort() #오름차순 정렬
print(a)
a.clear() #리스트 값 모두 삭제
print(a)
