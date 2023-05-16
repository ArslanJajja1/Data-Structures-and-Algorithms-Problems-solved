# Conflicting appointments
def conflicting_appointments(intervals):
    intervals.sort(key=lambda x:x[0])
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

print(conflicting_appointments([[1,4], [2,5], [7,9]]))
print(conflicting_appointments([[6,7], [2,4], [8,12]]))
print(conflicting_appointments([[4,5], [2,3], [3,6]]))

# TC : O(NLOGN)
# SC : O(N)