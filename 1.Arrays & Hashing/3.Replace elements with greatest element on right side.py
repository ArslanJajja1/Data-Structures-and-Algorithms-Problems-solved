# 1299. Replace Elements with Greatest Element on Right Side
# Easy
# 2.1K
# 198
# Companies
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 

# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # First Solution : Brute force is by using two loops  - O(n^2)

        # Second Solution : By using stack - TC : O(N) , SC : O(N)

        # n = len(arr)
        # stack = []
        # ans = [-1]*n
        # for i in range(n-1,-1,-1):
        #     if stack:
        #         ans[i] = stack[-1]
        #     if not stack:
        #         stack.append(arr[i])
        #     if stack and stack[-1] < arr[i]:
        #         stack.pop()
        #         stack.append(arr[i])
        # return ans

        # Third Solution : by using rightmax var to store max value, TC:O(N) , SC:O(1)
        n = len(arr)
        rightMax = -1
        ans = [None]*n
        for i in range(n-1,-1,-1):
            ans[i] = rightMax
            rightMax = max(rightMax,arr[i])
        return ans