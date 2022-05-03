
#2중 for문
'''
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()
'''
#문자열과 내장함수
msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)
print(tmp.find("T")) #T를 찾아라 , [I, T, , I, S, , T ~~], 1번 인덱스
print(tmp.count('T')) #T의 갯수, 2개

print(msg)
print(msg[:2]) #문자열 처음부터 2번 인덱스 전까지 추출, [0,1]
print(msg[3:5]) #3번,4번 인덱스 출력 [3,4]
print(len(msg)) #msg의 길이 공백포함

for i in range(len(msg)):
    print(msg[i], end=' ') #for문으로 msg 출력
print()

for x in msg:
    print(x, end=' ') #msg의 인덱스를 x가 한번씩 돔
print()

for x in msg:
    if x.isupper(): #x가 대문자이면 참, I T // islower(): 소문자면 참
        print(x, end=' ')
print()
for x in msg:
    if x.isalpha(): #알파벳만 출력
        print(x, end='')
print()
tmp='AZ'
for x in tmp:
    print(ord(x)) #ord: 아스키 넘버 출력

tmp=65
print(chr(tmp)) #숫자 > 문자 변환 (아스키)


