# Problem Statement #
# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]


def squared_sorted_array(arr):
    n = len(arr)-1
    left = 0
    right = n
    result = [None]*len(arr)
    k = n
    while left <= right:
        left_square = arr[left]*arr[left]
        right_square = arr[right]*arr[right]
        if left_square < right_square:
            result[k] = right_square
        else:
            result[k] = left_square
        k -= 1
    return result
            

print(squared_sorted_array([-2, -1, 0, 2, 3]))
print(squared_sorted_array([-3, -1, 0, 1, 2]))
