# 367. Valid Perfect Square
# Easy
# 3.6K
# 279
# Companies
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 

# Constraints:

# 1 <= num <= 231 - 1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i * i == num:
                return True
            if i* i > num:
                return False
    
    # TC : O(N)
    # SC : O(1)
    
    def isPerfectSquare_2(self, num: int) -> bool:
        l ,r = 1, num
        while l <= r:
            mid = (l +r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False

# TC : O(LOGN)
# SC : O(1)