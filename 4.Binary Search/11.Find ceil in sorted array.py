# Find ceil of an element in a sorted array

def find_ceil(nums,target):
    n = len(nums)
    if n == 0 or nums is None: return -1
    start = 0
    end = n-1
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    return res

print(find_ceil([2,4,5,6,8,9],7))
print(find_ceil([],7))
print(find_ceil([1],7))
print(find_ceil([7],7))
print(find_ceil([8],7))

# SC : O(1)
# TC : O(logn)
