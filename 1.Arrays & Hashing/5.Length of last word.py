# 58. Length of Last Word
# Easy
# 3.1K
# 163
# Companies
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)-1
        flag = False if s[-1] == ' ' else True
        count = 0
        while n >= 0:
            if s[n] == ' ' and flag == True:
                return count
            if s[n] != ' ':
                count += 1
                flag = True
            n -= 1
        return count
    # TC  : O(N)
    # SC : O(1)

        # Other solutions 
        #	return len(s.split()[-1])
        # c = 0
        # for i in s[::-1]:
        #     if i == " ":
        #         if c >= 1:
        #             return c
        #     else:
        #         c += 1
        # return c

