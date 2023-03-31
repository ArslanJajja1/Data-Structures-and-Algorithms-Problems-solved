# 84. Largest Rectangle in Histogram
# Hard
# 13.8K
# 192
# Companies
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4
 

# Constraints:

# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return heights[0]
        # if len(set(heights)) == 1:
        #     return n * heights[0]
        left = self.NSL(heights)
        right = self.NSR(heights)
        width = [None]*n
        area = [None]*n
        for i in range(n):
            width[i] = right[i] - left[i] - 1
        for j in range(n):
            area[j] = width[j] * heights[j]
        return max(area)

    # Nearest smaller to left 
    def NSL(self,arr:List[int])->List[int]:
        n = len(arr)
        output = [-1]*n
        stack = []
        for i in range(n):
            while len(stack) and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output[i] = -1
            if len(stack) > 0:
                output[i] = stack[-1]
            stack.append(i)
        return output
    # Nearest smaller to right
    def NSR(self,arr:List[int])->List[int]:
        n = len(arr)
        output = [-1]*n
        stack = []
        for i in range(n-1,-1,-1):
            while len(stack) and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output[i] = n
            if len(stack) > 0:
                output[i] = stack[-1]
            stack.append(i)
        return output
            

        