# 125. Valid Palindrome
# Easy
# 6.6K
# 6.9K
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(N) Space and O(n) Time solution

        # new_str = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         new_str += s[i].lower()
        # return new_str == new_str[::-1]

        # O(1) Space and O(n) Time solution : Two pointers
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and not self.alpha_num(s[left]):
                left += 1
            while right > left and not self.alpha_num(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            
    def alpha_num(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0')<=ord(c)<=ord('9') )
        