class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = []
        result = [-1]*n
        for i in range(n):
            sorted_intervals.append([intervals[i],i])
        sorted_intervals.sort(key=lambda x:x[0][0])
        for i in range(n):
            result[i] = self.binary_search(intervals[i][1],sorted_intervals)
        return result
    def binary_search(self,x,arr):
        n = len(arr)
        if arr[n-1][0][0] < x:
            return -1
        left = 0
        right = n-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid][0][0] >= x: right = mid-1
            else: left = mid + 1
        return arr[left][1]
    
    # TC : O(NLOGN)
    # SC : O(N)