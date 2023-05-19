# 303. Range Sum Query - Immutable
# Easy
# 2.8K
# 1.8K
# Companies
# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

# Example 1:

# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105
# 0 <= left <= right < nums.length
# At most 104 calls will be made to sumRange.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        rangeSum = 0
        for i in range(left,right+1):
            rangeSum += self.nums[i]
        return rangeSum
        # TC : O(N)
        # SC : O(1)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

        # TC : O(N)
        # SC : O(N)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum - leftSum

        # TC : O(1)
        # SC : O(1)


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)