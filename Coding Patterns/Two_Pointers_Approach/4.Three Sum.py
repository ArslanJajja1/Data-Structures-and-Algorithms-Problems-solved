# 15. 3Sum
# Medium
# 24.8K
# 2.2K
# Companies
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def threeSum( nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            find_pair(-nums[i],nums,i+1,output)
        return output
def find_pair(target,nums,left,output):
        right = len(nums)-1
        while left < right:
            if nums[left]+nums[right] == target:
                output.append([-target,nums[left],nums[right]])
                left += 1
                right -= 1
                while left<right and nums[left] == nums[left-1]:
                    left += 1
                while left<right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left]+nums[right] > target:
                right -= 1
            else:
                left += 1

# Time complexity #
# Sorting the array will take O(N∗logN). The searchPair() function will take O(N). As we are calling searchPair() for every number in the input array, this means that overall searchTriplets() will take O(N∗logN+N2), which is asymptotically equivalent to O(N​2​).

# Space complexity #
# Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.