# 713. Subarray Product Less Than K
# Medium
# 5.3K
# 169
# Companies
# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

from collections import deque
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        window_start = 0
        product = 1
        count = 0
        for window_end in range(len(nums)):
            product = product * nums[window_end]
            while product >= k and window_start < len(nums):
                product = product//nums[window_start]
                window_start += 1
            count += window_end-window_start+1
        return count
# TC : O(N)
# SC : O(1)