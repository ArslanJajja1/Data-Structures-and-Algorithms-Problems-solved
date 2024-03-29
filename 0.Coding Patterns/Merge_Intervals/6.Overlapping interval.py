# Overlapping interval
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        count = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] >= prev_end:
                prev_end = intervals[i][1]
            else:
                count += 1
                prev_end = min(prev_end,intervals[i][1])
        return count
            
# TC : O(NLOGN)
# SC : O(N)