# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

# Example 1:


# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 

# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(val) for val in row] for row in matrix]
        n = len(matrix)
        m = len(matrix[0])
        arr = [-1]*m
        for j in range(m):
            arr[j] = matrix[0][j]
        maximum = self.MAH(arr)
        for i in range(1,n):
            for j in range(0,m):
                if matrix[i][j] == 0:
                    arr[j] = 0
                else:
                    arr[j] = matrix[i][j] + arr[j]
            maximum = max(maximum,self.MAH(arr))
        return maximum

    # Maximum area histogram ( MAH )
    def MAH(self,arr:List[int])->List[int]:
        n = len(arr)
        left = self.NSL(arr)
        right = self.NSR(arr)
        width = [-1]*n
        area = [-1]*n
        for i in range(n):
            width[i] = right[i]-left[i]-1
        for j in range(n):
            area[j] = width[j]*arr[j]
        return max(area)

    # Nearest smaller left
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
    # Nearest smaller right
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




