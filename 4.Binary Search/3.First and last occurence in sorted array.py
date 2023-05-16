# 34. Find First and Last Position of Element in Sorted Array
# Medium
# 16.4K
# 393
# Companies
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
# nums is a non-decreasing array.
# -109 <= target <= 109

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occurence = self.find_first_occurence(nums,target)
        last_occurence = self.find_last_occurence(nums,target)
        return [first_occurence,last_occurence]
    # Find first occurence
    def find_first_occurence(self,arr,target):
        start = 0
        end = len(arr)-1
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if target == arr[mid]:
                result = mid
                end = mid - 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return result
    # Find last occurence
    def find_last_occurence(self,arr,target):
        start = 0
        end = len(arr)-1
        result = -1
        while start <= end:
            mid = start + (end-start)//2
            if target == arr[mid]:
                result = mid
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return result

# SC : O(1)
# TC : O(logn)