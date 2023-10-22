# Problem Statement #
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.

def find_longest_subarray(arr,k):
    max_ones = 0
    window_start = 0
    longest_subarray = 0
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones += 1
        while (window_end-window_start+1) - max_ones > k:
            if arr[window_start] == 1:
                max_ones -= 1
            window_start += 1
        longest_subarray = max(longest_subarray,window_end-window_start+1)
    return longest_subarray
print(find_longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2))
print(find_longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3))

# Time Complexity : O(N)
# Space Complexity : O(1)
