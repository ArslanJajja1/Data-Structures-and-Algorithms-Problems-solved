# Find the index of first 1 in a binary sorted array

def find_ones_index(nums):
    start = 0
    end = 1
    res = -1
    while nums[end] < 1:
        start = end
        end *= 2
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == 1:
            res = mid
            end = mid - 1
        elif nums[mid] < 1:
            start = mid + 1
    return res

print(find_ones_index([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])) # Infinite binary sorted array

# SC : O(1)
# TC : O(logn)