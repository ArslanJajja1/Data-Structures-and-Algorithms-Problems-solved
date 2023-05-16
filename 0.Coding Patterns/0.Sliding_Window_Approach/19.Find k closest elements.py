# 658. Find K Closest Elements
# Medium
# 6.9K
# 559
# Companies
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
 

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]
 

# Constraints:

# 1 <= k <= arr.length
# 1 <= arr.length <= 104
# arr is sorted in ascending order.
# -104 <= arr[i], x <= 104

import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ## Heap solution : O(NLOGK)

        # heap = []
        # ans = []
        # for i in range(len(arr)):
        #     diff = abs(arr[i]-x)
        #     heapq.heappush(heap,(-1*diff,-arr[i]))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # while heap:
        #     diff,closest = heapq.heappop(heap)
        #     ans.append(-1*closest)
        # ans.sort()
        # return ans

        # Binary search solution : O(LOG(N-K)+K)
        
        left = 0
        right = len(arr)-k
        while left < right:
            mid = left + (right-left)//2
            if x-arr[mid] > arr[mid+k]-x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]



        