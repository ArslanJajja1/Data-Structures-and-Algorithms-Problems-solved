# 219. Contains Duplicate II
# Easy
# 4.8K
# 2.6K
# Companies
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window_start = 0
        window = set()
        for window_end in range(len(nums)):
            if window_end-window_start > k:
               window.remove(nums[window_start])
               window_start += 1
            if nums[window_end] in window:
                return True
            window.add(nums[window_end])
        return False

# TC : O(N)
# SC : O(N)