# プログラミングの宝箱 アルゴリズムとデータ構造 第2版
# https://amzn.to/2p3hS3w
# P30~
def mergeSort(n, x, offset):
    if n <= 1:
        return
    m = n // 2

    mergeSort(m, x, offset)
    mergeSort(n - m, x, offset + m)

    buffer = [0 for i in range(m)]
    for i in range(m):
        buffer[i] = x[offset + i]
    
    j = m
    i = 0
    k = 0
    while i < m and j < n:
        if buffer[i] <= x[offset + j]:
            x[offset + k] = buffer[i]
            k += 1
            i += 1
        else:
            x[offset + k] = x[offset + j]
            k += 1
            j += 1
    
    while i < m:
        x[offset + k] = buffer[i]
        k += 1
        i += 1

arr = [i for i in range(5)]
arr.sort(key=lambda x: -x)
print(arr)
mergeSort(len(arr), arr, 0)
print(arr)