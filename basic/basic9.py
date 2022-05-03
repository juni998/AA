#2차원 리스트 생성, 접근

'''
a=[0]*10 # 1차원 리스트 길이: 10
print(a)
'''

a=[[0]*3 for _ in range(3)] #2차원 리스트 생성
print(a)
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

for x in a:
    print(x)

for x in a:
    for y in x:
        print(y, end=' ') #2차원 배열 출력
    print()