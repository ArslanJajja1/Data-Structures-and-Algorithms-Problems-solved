# Find kth positive
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # First Approach

        # missing_count = 0
        # for i in range(len(arr)):
        #     if arr[i] - i - 1 >= k:
        #         return i + k
        #     else:
        #         missing_count = arr[i] - i - 1
        # return arr[-1] + k - missing_count

        # Second Approach
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            missing_count = arr[mid] - (mid + 1)
            if missing_count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k

# TC : O(LOGN)
# SC : O(1)