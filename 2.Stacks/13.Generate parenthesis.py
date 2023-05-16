# 22. Generate Parentheses
# Medium
# 17.4K
# 703
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        def solve(s,open,close):
            if open > close:
                return
            if open == 0 and close == 0:
                output.append(s)
                return
            if open > 0 :
                solve(s+"(",open-1,close)
            if close > 0:
                solve(s+")",open,close-1)
        solve("",n,n)
        return output
        
        