# 1888. Minimum Number of Flips to Make the Binary String Alternating
# Medium
# 965
# 37
# Companies
# You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

# Type-1: Remove the character at the start of the string s and append it to the end of the string.
# Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
# Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

# The string is called alternating if no two adjacent characters are equal.

# For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

# Example 1:

# Input: s = "111000"
# Output: 2
# Explanation: Use the first operation two times to make s = "100011".
# Then, use the second operation on the third and sixth elements to make s = "101010".
# Example 2:

# Input: s = "010"
# Output: 0
# Explanation: The string is already alternating.
# Example 3:

# Input: s = "1110"
# Output: 1
# Explanation: Use the second operation on the second element to make s = "1010".
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        alt1 = ""
        alt2 = ""
        for i in range(len(s)):
            alt1 += "1" if i%2 else "0"
            alt2 += "0" if i%2 else "1"

        window_start = 0
        diff1 = 0
        diff2 = 0
        res = len(s)
        for window_end in range(len(s)):
            if s[window_end] != alt1[window_end]:
                diff1 += 1
            if s[window_end] != alt2[window_end]:
                diff2 += 1
            if window_end - window_start +1 > n:
                if s[window_start] != alt1[window_start]:
                    diff1 -= 1
                if s[window_start] != alt2[window_start]:
                    diff2 -= 1
                window_start += 1
            if window_end-window_start+1 == n:
                res = min(res,diff1,diff2)
        return res
# TC : O(N)
# SC : O(N)
