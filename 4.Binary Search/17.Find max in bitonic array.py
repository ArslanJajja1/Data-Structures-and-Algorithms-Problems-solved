# 852. Peak Index in a Mountain Array
# Medium
# 4.9K
# 1.8K
# Companies
# An array arr a mountain if the following properties hold:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

 

# Example 1:

# Input: arr = [0,1,0]
# Output: 1
# Example 2:

# Input: arr = [0,2,1,0]
# Output: 1
# Example 3:

# Input: arr = [0,10,5,2]
# Output: 1
 

# Constraints:

# 3 <= arr.length <= 105
# 0 <= arr[i] <= 106
# arr is guaranteed to be a mountain array.

 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        start = 0
        end = n-1

        while start <= end:
            mid = start + (end-start)//2
            if mid > 0 and mid < n-1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid+1] > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if mid == 0:
                    if nums[mid] > nums[mid+1]:
                        return mid
                    else:
                        return mid+1
                if mid == n-1:
                    if nums[mid] > nums[mid-1]:
                        return mid
                    else:
                        return mid-1
            
        
# SC : O(1)
# TC : O(logn)