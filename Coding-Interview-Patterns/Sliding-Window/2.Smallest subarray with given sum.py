# Smallest Subarray with a given sum (easy)

# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

def find_smallest_subarray(arr,S):
    window_start = 0
    window_end = 0
    window_sum = 0
    min_length = float('inf')
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= S:
            min_length = min(min_length,window_end-window_start+1)
            window_sum -= arr[window_start]
            window_start += 1
    return min_length


print(find_smallest_subarray([2, 1, 5, 2, 3, 2],7))
print(find_smallest_subarray([2, 1, 5, 2, 8],7))
print(find_smallest_subarray([3, 4, 1, 1, 6],7))

# Time Complexity : O(N)
# Space Complexity : O(1)