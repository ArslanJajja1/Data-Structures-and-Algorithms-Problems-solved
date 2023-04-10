# Circular array loop
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            is_forward = nums[i]>=0
            slow = fast = i
            while True:
                slow = self.find_next_index(nums,is_forward,slow)
                fast = self.find_next_index(nums,is_forward,fast)
                if fast != -1:
                    fast = self.find_next_index(nums,is_forward,fast)
                if slow == -1 or fast == -1 or slow == fast:
                    break
            if slow != -1 and slow == fast:
                return True
        return False
    def find_next_index(self,nums,is_forward,curr_index):
        direction = nums[curr_index] >= 0
        if direction != is_forward:
            return -1
        next_index = (curr_index + nums[curr_index])%len(nums)
        if curr_index == next_index:
            next_index = -1
        return next_index
# TC : O(N^2)
# SC : O(1)