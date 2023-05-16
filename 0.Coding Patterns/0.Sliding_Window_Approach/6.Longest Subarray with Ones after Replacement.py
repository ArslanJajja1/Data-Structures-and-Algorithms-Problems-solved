# ​‌‍‌⁡⁣⁣⁢Problem Statement #⁡​
# ⁡⁣⁢⁣Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.⁡

# ⁡⁣⁣⁢Example 1:⁡

# ⁡⁣⁢⁣Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.⁡

# ⁡⁣⁣⁢Example 2:
# ⁡
# ⁡⁣⁢⁣Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.⁡

import math


def longest_subarray(arr: [int], k: int) -> int:
    window_start = 0
    max_length = -math.inf
    ones = 0

    for window_end in range(len(arr)):
        num = arr[window_end]
        if num == 1:
            ones += 1
        while (window_end - window_start + 1) - ones > k:
            left_num = arr[window_start]
            if left_num == 1:
                ones -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(longest_subarray([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest_subarray([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))

# ⁡⁢⁣⁣ Time Complexity⁡ : ⁡⁣⁢⁣The time complexity of the above algorithm will be (N) where ‘N’ is the count of numbers in the input array.⁡

# ⁡⁢⁣⁣ Space Complexity⁡ : ⁡⁣⁢⁣The algorithm runs in constant space (1).⁡
