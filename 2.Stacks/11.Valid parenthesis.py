# 20. Valid Parentheses
# Easy
# 18.7K
# 1.1K
# Companies
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        n = len(s)
        for i in range(n):
            if s[i] == "[" or s[i] == "{" or s[i] == "(":
                stack.append(s[i])
            if s[i] in hashmap:
                if stack and hashmap[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

