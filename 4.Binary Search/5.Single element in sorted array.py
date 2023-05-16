# Find single element in sorted array

def find_single_element(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        mid = start + (end-start)//2
        if mid % 2 == 1:
            mid = mid - 1
        if arr[mid] != arr[mid+1]:
            end = mid
        else:
            start = mid + 2
    return arr[start]

print(find_single_element([2,2,3,3,4,4,5,6,6,7,7]))
print(find_single_element([1, 1, 2, 3, 3, 4, 4, 6, 6]))

# SC : O(1)
# TC : O(logn)
