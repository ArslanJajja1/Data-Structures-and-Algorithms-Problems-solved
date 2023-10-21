# Problem Statement #
# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def find_max_sum(arr,k):
    window_start = 0
    window_end = 0
    window_sum = 0
    max_sum = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum,window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

print(find_max_sum([2, 1, 5, 1, 3, 2],3))
print(find_max_sum([2, 3, 4, 1, 5],2))

# Time Complexity : O(N)
# Space Complexity : O(1)
