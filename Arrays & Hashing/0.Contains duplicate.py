# 217. Contains Duplicate
# Easy
# 9.1K
# 1.2K
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:

    ## First Method - Using two for loops - Time O(n^2) - Space O(1)

    def containsDuplicate(self, nums: List[int]) -> bool:
    #     if (nums == None or len(nums)==0): return False
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]==nums[j]:
    #                 return True
    #     return False

    ## Second Method - Using sorting - Time O(nlogn) - Space O(1)

        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False

    ## Third Method - using sets - Time O(n) - Space O(n)

        # unique_nums = {s for s in nums}
        # if len(unique_nums)==len(nums):
        #     return False
        # return True

    ## Fourth Method - Using hashmaps - Time O(n) - Space O(n)

        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                 hashmap[nums[i]]=1
            else:
                return True
        return False
