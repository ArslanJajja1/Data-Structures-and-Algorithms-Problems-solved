# Problem Statement #
# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# Example 1:

# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]
# Example 2:

# Input: [2, 2, 0, 1, 2, 0]
# Output: [0 0 1 2 2 2 ]
def dutch_flag_sort(nums):
    n = len(nums)
    left = 0
    right = n-1
    i=0
    while i <= right:
        if nums[i] == 0:
            nums[left],nums[i] = nums[i],nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right],nums[i] = nums[i],nums[right]
            right -= 1
        else:
            i += 1
    return nums


print(dutch_flag_sort([1, 0, 2, 1, 0]))
print(dutch_flag_sort([2, 2, 0, 1, 2, 0]))
