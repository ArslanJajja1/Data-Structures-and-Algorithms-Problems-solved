# Number of times a sorted array is rotated

def rotated_array_count(nums):
    n = len(nums)
    if not nums or len(nums) == 0: return -1
    if n==1 or nums[0] < nums[n-1]:
        return 0
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        prev = (mid - 1 + n) % n
        nxt = (mid + 1 + n) % n
        if nums[mid] < nums[prev] and nums[mid] < nums[nxt]:
            return mid
        elif nums[start] <= nums[mid]:
            start = mid + 1
        else:
            end = mid - 1

print(rotated_array_count([8,9,10,1,2,3,4,5,6,7]))
print(rotated_array_count([0,1,2,3,4,5,6,7]))
print(rotated_array_count([1]))
print(rotated_array_count([]))
print(rotated_array_count([5,6,7,2,4]))

# SC : O(1)
# TC : O(n)