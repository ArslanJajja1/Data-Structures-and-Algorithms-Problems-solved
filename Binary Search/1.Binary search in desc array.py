# Binary search in descending order sorted array

def binary_search(arr,target):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = start + (end-start)//2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
# SC : O(1)
# TC : O(n)
