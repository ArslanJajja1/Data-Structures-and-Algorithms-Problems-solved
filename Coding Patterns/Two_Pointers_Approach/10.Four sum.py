# Quadruple Sum to Target (medium) #
# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# Example 1:

# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Example 2:

# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

def four_sum(nums,target):
    nums.sort()
    n = len(nums)
    output = []
    for i in range(n-3):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and nums[j] == nums[j-1]:
                continue
            find_pair(nums,target,i,j,output)
    return output
def find_pair(nums,target,first,second,output):
    n = len(nums)
    left = second+1
    right = n-1
    while left < right:
        current_sum = nums[first]+nums[second]+nums[left]+nums[right]
        if current_sum == target:
            output.append([nums[first],nums[second],nums[left],nums[right]])
            left +=1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
print(four_sum([4, 1, 2, -1, 1, -3],1))
print(four_sum([2, 0, -1, 1, -2, 2],2))
# Time complexity #
# Sorting the array will take O(N∗logN). Overall searchQuadruplets() will take O(N∗logN+N3), which is asymptotically equivalent to O(N3).

# Space complexity #
# The space complexity of the above algorithm will be O(N) which is required for sorting.