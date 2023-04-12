# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        ans = []
        while i < n:
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i += 1
        for k in range(n):
            if nums[k] != k+1:
                ans.append(k+1)
        return ans
# TC : O(N)
# SC : O(1)