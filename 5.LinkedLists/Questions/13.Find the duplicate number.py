class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Using cyclic sort

        # i = 0
        # n = len(nums)
        # while i < n:
        #     j = nums[i]-1
        #     if nums[i] != nums[j]:
        #         nums[i],nums[j] = nums[j],nums[i]
        #     else:
        #         i += 1
        # for k in range(n):
        #     if nums[k] != k+1:
        #         return nums[k]
        # return -1

        # using slow and fast pointers

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                return slow
            
# TC : O(N)
# SC : O(1)