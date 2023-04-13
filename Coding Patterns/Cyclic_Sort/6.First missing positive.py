#Find the Smallest Missing Positive Number (medium) #

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(n):
            val = abs(nums[j])
            if 1 <= val <= n:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (n+1)
        for k in range(1,n+1):
            if nums[k-1] >= 0:
                return k
        return n+1
# TC : O(N)
# SC : O(1)
