# Maximum CPU Load
from heapq import *
def maximum_cpu_load(jobs):
    jobs.sort(key=lambda x:x[0])
    max_load = current_load = 0
    min_heap = []
    for i in range(len(jobs)):
        while len(min_heap)>0 and jobs[i][0] >= min_heap[0][1]:
            current_load -= min_heap[0][2]
            heappop(min_heap)
        heappush(min_heap,jobs[i])
        current_load += jobs[i][2]
        max_load = max(current_load,max_load)
    return max_load

print(maximum_cpu_load([[1,4,3], [2,5,4], [7,9,6]]))
print(maximum_cpu_load([[6,7,10], [2,4,11], [8,12,15]]))
print(maximum_cpu_load( [[1,4,2], [2,4,1], [3,6,5]]))

# TC : O(NLOGN)
# SC : O(N)