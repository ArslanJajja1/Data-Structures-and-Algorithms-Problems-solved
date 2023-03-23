# 1493. Longest Subarray of 1's After Deleting One Element
# Medium
# 1.4K
# 30
# Companies
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

def longestSubarray(nums: List[int]) -> int:
        window_start = 0
        max_ones = 0
        zeros = 0
        max_length = 0
        for window_end in range(len(nums)):
            right_num = nums[window_end]
            if right_num == 1:
                max_ones += 1
            if right_num == 0:
                zeros += 1
            while zeros > 1:
                left_num = nums[window_start]
                if left_num == 1:
                    max_ones -= 1
                if left_num == 0:
                    zeros -= 1
                window_start += 1
            max_length = max(max_length,window_end-window_start)
        return max_length