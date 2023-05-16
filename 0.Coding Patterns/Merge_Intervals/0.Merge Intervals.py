#56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge_intervals = []
        intervals.sort(key=lambda x:x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1],end)
            else:
                merge_intervals.append([start,end])
                start = interval[0]
                end = interval[1]
        merge_intervals.append([start,end])
        return merge_intervals

# TC : O(NLOGN)
# SC : O(N)