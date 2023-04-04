# Minimum difference element in a sorted array

def find_minimum_difference(nums,target):
    n = len(nums)
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if start == n:
        return nums[n-1]
    if end == -1:
        return nums[0]
    if abs(target-nums[start]) < abs(target-nums[end]):
        return nums[start]
    else:
        return nums[end]


print(find_minimum_difference([1,2,3,4,7,9,12,14,17,24,37,40],26))
print(find_minimum_difference([2, 5, 10, 12, 15],6))
print(find_minimum_difference([2, 5, 10, 12, 15],5))
print(find_minimum_difference([2, 5, 10, 12, 15],8))
print(find_minimum_difference([2, 5, 10, 12, 15],11))
print(find_minimum_difference([2, 5, 10, 12, 15],20))
print(find_minimum_difference([2, 5, 10, 12, 15],1))

# SC : O(1)
# TC : O(logn)