# Find floor of an element in sorted array

def find_floor(nums,target):
    n = len(nums)
    if n == 0 or nums is None:
        return -1
    if n==1:
        if nums[0] == target: return 0
        elif nums[0] > target: return -1
        else: return 0
        
    start = 0
    end = n-1
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

print(find_floor([2,4,5,6,8,9],7))
print(find_floor([],7))
print(find_floor([1],7))
print(find_floor([7],7))


# SC : O(1)
# TC : O(logn)