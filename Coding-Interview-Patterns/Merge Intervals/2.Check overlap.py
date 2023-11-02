# Problem 1: Given a set of intervals, find out if any two intervals overlap.

# Example:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: true
# Explanation: Intervals [1,4] and [2,5] overlap

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def print_interval(self):
        print([self.start,self.end])
def check_overlap(intervals):
    if len(intervals) < 2:
        return False
    intervals.sort(key=lambda x:x.start)
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1,len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            return True
        else:
            start = interval.start
            end = interval.end
    return False


if check_overlap([Interval(1,4),Interval(2,5),Interval(7,9)]):
    print('Overlapping.')

if check_overlap([Interval(1,4),Interval(2,5),Interval(7,9)]):
    print('No Overlapping.')

# Time Complexity : O(NLOGN)
# Space Complexity : O(N)