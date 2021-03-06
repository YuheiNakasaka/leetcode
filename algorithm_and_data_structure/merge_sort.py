# sort済み用のArrayを使うのでメモリ領域を消費するが実装はシンプル
# https://www.codereading.com/algo_and_ds/algo/merge_sort.html
def merge_sort(aList):
    if len(aList) <= 1:
        return aList
    
    mid = len(aList) // 2
    left = aList[:mid]
    right = aList[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    if left:
        sorted_list.extend(left[left_index:])
    if right:
        sorted_list.extend(right[right_index:])

    return sorted_list



l = [1,3,2,4,5,7,6,10,8,9]
print(l)
l = merge_sort(l)
print(l)