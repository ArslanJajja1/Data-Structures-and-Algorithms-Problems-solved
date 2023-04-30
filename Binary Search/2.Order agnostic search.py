# Order agnostic search | Order not known search

def order_agnostic_search(arr,target):
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    if arr[0] > arr[len(arr)-1]:
        binary_search_desc(arr,target)
    if arr[0] <= arr[len(arr)-1]:
        binary_search_asc(arr,target)
# Binary search in ascending order sorted array
def binary_search_asc(arr,target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
def binary_search_desc(arr,target):
    start = 0
    end = 0
    while start <= end:
        mid = start + (end-start)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

# SC : O(1)
# TC : 0(logn)