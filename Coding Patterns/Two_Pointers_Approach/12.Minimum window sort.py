# Minimum Window Sort (medium) #
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:

# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

def minimum_window_sort(nums):
    n = len(nums)
    left = 0
    right = n-1
    while left < n-1 and nums[left] <= nums[left+1]:
        left += 1
    if left == n:
        return True
    while right >=0 and nums[right] >= nums[right-1]:
        right -= 1
    min_item = float('inf')
    max_item = float('-inf')
    for k in range(left,right+1):
        min_item = min(min_item,nums[k])
        max_item = max(max_item,nums[k])
    while left > 0 and nums[left-1] > min_item:
        left -= 1
    while right < n-1 and nums[right+1] <  max_item:
        right += 1
    return right-left+1

    
            

print(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimum_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(minimum_window_sort([1, 2, 3]))
print(minimum_window_sort([3, 2, 1]))

# Time complexity #
# The time complexity of the above algorithm will be O(N).

# Space complexity #
# The algorithm runs in constant space O(1).