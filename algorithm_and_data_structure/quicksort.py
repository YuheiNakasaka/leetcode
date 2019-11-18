# プログラミングの宝箱 アルゴリズムとデータ構造 第2版
# https://amzn.to/2p3hS3w
# P8~
import random
N = 10
arr = [random.randrange(100) for _ in range(N)]

def quicksort(bottom, top, data):
    if bottom > top:
        return
    
    div = data[bottom]

    lower = bottom
    upper = top
    while lower < upper:
        while lower <= upper and data[lower] <= div:
            lower += 1
        while lower <= upper and data[upper] >= div:
            upper -= 1
        if lower < upper:
            tmp = data[lower]
            data[lower] = data[upper]
            data[upper] = tmp

    tmp = data[bottom]
    data[bottom] = data[upper]
    data[upper] = tmp

    quicksort(bottom, upper - 1, data)
    quicksort(upper + 1, top, data)

def quicksort2(bottom, top, data):
    if bottom < top:
        lower = bottom
        upper = top
        div = data[top//2]
        while 1:
            while data[lower] < div:
                lower += 1
            while data[upper] > div:
                upper -= 1
            if lower >= upper:
                break
            tmp = data[lower]
            data[lower] = data[upper]
            data[upper] = tmp
            lower += 1
            upper -= 1
        quicksort2(bottom, lower - 1, data)
        quicksort2(lower + 1, top, data)

print('quicksort1')
print(arr)
quicksort(0, N - 1, arr)
print(arr)

print('quicksort2')
print(arr)
quicksort2(0, N - 1, arr)
print(arr)