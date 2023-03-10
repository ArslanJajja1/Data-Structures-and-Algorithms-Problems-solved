# ​‌‍‌⁡⁣⁣⁢Problem Statement #⁡​
# ⁡⁢⁣⁣Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.⁡

# ⁡⁣⁢⁣ ⁡⁢⁣⁣Example 1⁡:

# ⁡⁣⁢⁡⁣⁢⁣Input: [2, 1, 5, 2, 3, 2], S=7 ⁡
# ⁡⁣⁢⁣Output: 2⁡
# ⁡⁣⁢⁣Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].⁡

# ⁡⁢⁣⁣Example 2⁡:

# ⁡⁣⁢⁣Input: [2, 1, 5, 2, 8], S=7 ⁡
# ⁡⁣⁢⁣Output: 1⁡
# ⁡⁣⁢⁣Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].⁡

# ⁡⁢⁣⁣Example 3:⁡

# ⁡⁣⁢⁣Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].⁡

# ⁡⁣⁣ ⁡⁣⁣⁢Brute Force :⁡
import math


def smallest_subarray_bf(arr, s):
    minLength = math.inf
    for i in range(len(arr)):
        windowLength = 0
        windowSum = 0
        for j in range(i, len(arr)):
            windowSum += arr[j]
            windowLength += 1
            if windowSum >= s:
                minLength = min(windowLength, minLength)
                break
    return minLength


print("Brute force solution ---> ")

print(smallest_subarray_bf([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_bf([2, 1, 5, 2, 8], 7))
print(smallest_subarray_bf([3, 4, 1, 1, 6], 8))

# ⁡⁢⁣⁣Time Complexity :⁡ ⁡⁣⁢⁣The time complexity for this solution will be O(n^2) because we are using nested loops to find the min length for each subarray. For each n, the nested loop run n times ;⁡

# ⁡⁢⁣⁣Space Complexity ⁡: ⁡⁣⁢⁣The space complexity for this solution will be O(1)  which is a constant time because we are not using any extra space in this solution ;⁡

# ⁡⁣⁣⁢Optimized solution using sliding window approach⁡ :


def smallest_subarray_optimized(arr, s):
    windowStart, windowSum = 0, 0
    minLength = math.inf
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        while windowSum >= s:
            minLength = min(minLength, windowEnd-windowStart+1)
            windowSum -= arr[windowStart]
            windowStart += 1
    return minLength


print("Optimized solution ---> ")
print(smallest_subarray_optimized([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_optimized([2, 1, 5, 2, 8], 7))
print(smallest_subarray_optimized([3, 4, 1, 1, 6], 8))


#  ⁡⁢⁣⁣Time Complexity⁡⁡ : ⁡⁣⁢⁣The time complexity for this solution will be O(n) which will be linear time as we are looping through the arrar only once ; ⁡

# ⁡⁢⁣⁣Space Complexity ⁡: T⁡⁣⁢⁣he space complexity for the above solution will be 0(1) which is a constant time as we are not using any extra space ;⁡
