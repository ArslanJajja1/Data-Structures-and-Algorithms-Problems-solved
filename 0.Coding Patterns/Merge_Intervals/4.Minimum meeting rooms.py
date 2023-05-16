# Minimum meeting rooms
from heapq import *
# First Approach : min heap
def minimum_meeting_rooms(meetings):
    meetings.sort(key=lambda x:x[0])
    meeting_rooms = 0
    min_heap = []
    for i in range(len(meetings)):
        while len(min_heap) > 0 and meetings[i][0] >= min_heap[0][1]:
            heappop(min_heap)
        heappush(min_heap,meetings[i])
        meeting_rooms = max(meeting_rooms,len(min_heap))
    return meeting_rooms
print(minimum_meeting_rooms([[1,4], [2,5], [7,9]]))
print(minimum_meeting_rooms([[6,7], [2,4], [8,12]]))
print(minimum_meeting_rooms([[1,4], [2,3], [3,6]]))
print(minimum_meeting_rooms([[4,5], [2,3], [2,4], [3,5]]))

# Second Approach : two arrays

def count_meeting_rooms(meetings):
    start = sorted([i[0] for i in meetings])
    end = sorted([i[1] for i in meetings])
    s = e = 0
    res = count = 0
    while s < len(meetings):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res,count)
    return res

print(count_meeting_rooms([[1,4], [2,5], [7,9]]))
print(count_meeting_rooms([[6,7], [2,4], [8,12]]))
print(count_meeting_rooms([[1,4], [2,3], [3,6]]))
print(count_meeting_rooms([[4,5], [2,3], [2,4], [3,5]]))