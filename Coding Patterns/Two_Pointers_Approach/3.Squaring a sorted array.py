# Problem Statement #
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]

def squares_of_sorted_array(nums):
    n = len(nums)
    output = [0]*n
    idx = n-1
    left = 0
    right = n-1
    while left<=right:
        left_square = nums[left]*nums[left]
        right_square = nums[right]*nums[right]
        if left_square>right_square:
            output[idx] = left_square
            left += 1
            idx -= 1
        else:
            output[idx] = right_square
            right -= 1
            idx -= 1
    return output

print(squares_of_sorted_array([-2, -1, 0, 2, 3]))
print(squares_of_sorted_array([-3, -1, 0, 1, 2]))

# Time complexity #
# The time complexity of the above algorithm will be O(N) as we are iterating the input array only once.

# Space complexity #
# The space complexity of the above algorithm will also be O(N); this space will be used for the output array.