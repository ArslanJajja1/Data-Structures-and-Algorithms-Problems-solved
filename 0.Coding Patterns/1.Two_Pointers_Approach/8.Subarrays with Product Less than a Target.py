# Problem Statement #
# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

# Example 1:

# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50 
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
# Explanation: There are seven contiguous subarrays whose product is less than the target.
from collections import deque
def subarrays(nums,target):
    window_start = 0
    product = 1
    output = []
    for window_end in range(len(nums)):
        product *= nums[window_end]
        while product >= target and window_start < len(nums):
            product /= nums[window_start]
            window_start += 1
        temp_list = deque()
        for i in range(window_end,window_start-1,-1):
            temp_list.appendleft(nums[i])
            output.append(list(temp_list))
    return output

print(subarrays( [2, 5, 3, 10],30 ))
print(subarrays( [8, 2, 6, 5],50 ))

# Time complexity #
# The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N2) in the worst case. Therefore overall, our algorithm will take O(N3).

# Space complexity #
# Ignoring the space required for the output list, the algorithm runs in O(N) space which is used for the temp list.