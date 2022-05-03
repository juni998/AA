#함수 만들기
'''
def add(a, b): #함수 선언
    c=a+b
    print(c)

add(3, 2) #함수 호출


def add(a, b):
    c=a+b
    return c

print(add(3, 2))


def add(a, b):
    c=a+b
    d=a-b
    return c, d #튜플 구조로 리턴

print(add(3, 2))
'''
def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
