# ​‌‍⁡⁣⁣​‌‍‌⁡⁣⁣⁢𝗣𝗿𝗼𝗯𝗹𝗲𝗺 𝗦𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁 ⁡​
#
# ⁡⁢⁣⁣Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.⁡

# ⁡⁣⁢⁣Example 1:⁡

# ⁡⁣⁢⁣ Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# Example 2:

# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].⁡

# ⁢ ⁡⁣⁣⁢Brute Force Way to solve this question ⁡⁡⁡

def maxSumSubarray(arr, k):
    maxSum = 0
    for i in range(len(arr)-k+1):
        windowSum = 0
        for j in range(i, i+k):
            windowSum += arr[j]
        maxSum = max(windowSum, maxSum)
    return maxSum


print(maxSumSubarray([2, 1, 5, 1, 3, 2], 3))
print(maxSumSubarray([2, 3, 4, 1, 5], 2))

# ⁡⁢⁣⁣Time Complexity⁡ : T⁡⁣⁢⁣he time complexity for this solution will be o(n^2) because we are using nested loops in the solution to find the window sum ;⁡

# ⁡⁢⁣⁣Space Complexity ⁡: T⁡⁣⁢⁣he space complexity for this solution will be O(1) which is a constant time because we are not using any extra space ;⁡