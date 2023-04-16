import random

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr,start,mid)
        merge_sort(arr, mid+1,end)
        merge(arr,start, mid, end)

def merge(arr,start,mid,end):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    leftidx = 0
    rightidx = 0
    
    while leftidx < len(left) and rightidx < len(right):
        if left[leftidx] < right[rightidx]:
            arr[start] = left[leftidx]
            leftidx += 1
        else:
            arr[start] = right[rightidx]
            rightidx += 1
        start += 1
    while leftidx < len(left):
        arr[start] = left[leftidx]
        leftidx += 1
        start += 1
    while rightidx < len(right):
        arr[start] = right[rightidx]
        rightidx += 1
        start += 1
    
    
            
# A=[random.randint(-100,100) for i in range(10)]
# print(A)
# merge_sort(A, 0, len(A) - 1)
# print(A)

def is_sorted(lst):
    return lst == sorted(lst)

for _ in range(30):
    A=[random.randint(-100,100) for i in range(100)]
    merge_sort(A, 0, len(A) - 1)
    print(is_sorted(A))

