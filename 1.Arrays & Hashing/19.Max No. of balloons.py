# 1189. Maximum Number of Balloons
# Easy
# 1.4K
# 83
# Companies
# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = len(text)  # or float("inf")
        for c in balloon:
            res = min(res, countText[c] // balloon[c])
        return res
# TC : O(N)
# SC : O(N)