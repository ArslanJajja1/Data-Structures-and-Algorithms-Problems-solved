class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # First Approach

    #     i = 0
    #     merged = []
    #     while i < len(intervals):
    #         interval = intervals[i]
    #         if newInterval[0] < interval[0]:
    #             intervals.insert(i,newInterval)
    #             break
    #         i += 1
    #     if i == len(intervals):
    #         intervals.append(newInterval)
    #     self.merge_intervals(intervals,merged)
    #     return merged
    # def merge_intervals(self,intervals,merged):
    #     start = intervals[0][0]
    #     end = intervals[0][1]
    #     for i in range(1,len(intervals)):
    #         interval = intervals[i]
    #         if interval[0] <= end:
    #             end = max(end,interval[1])
    #         else:
    #             merged.append([start,end])
    #             start = interval[0]
    #             end = interval[1]
    #     merged.append([start,end])

    # Second Appraoch
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                start = min(newInterval[0],intervals[i][0])
                end = max(newInterval[1],intervals[i][1])
                newInterval = [start,end]
        res.append(newInterval)
        return res

# TC : O(N)
# SC : O(N)