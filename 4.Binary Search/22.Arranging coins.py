# 441. Arranging Coins
# Easy
# 3.3K
# 1.2K
# Companies
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1cs

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Linear time solution : O(N)

        # coins = n
        # for i in range(1,n+1):
        #     coins -= i
        #     if coins == 0:
        #         return i
        #     if coins < 0:
        #         return i-1

        # Binary search solution : O(LOGN)
        left = 1
        right = n
        res = 0
        while left <= right:
            mid = left + (right-left)//2
            coins = (mid/2)*(mid+1)
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                res = max(res,mid)
        return res
                

