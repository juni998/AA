#최솟값 구하기

arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf') # 가장큰값

for i in range(len(arr)):
    if arrMin > arr[i]:
        arrMin = arr[i]
