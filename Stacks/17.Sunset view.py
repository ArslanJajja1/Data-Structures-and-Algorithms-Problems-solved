# Given an array representing heights of buildings. The array has buildings from left to right as shown in below diagram, count number of buildings facing the sunset. It is assumed that heights of all buildings are distinct.

# Examples: 

# Input : arr[] = {7, 4, 8, 2, 9}
# Output: 3
# Explanation: As 7 is the first element, it can 
# see the sunset.
# 4 can't see the sunset as 7 is hiding it. 
# 8 can see.
# 2 can't see the sunset.
# 9 also can see the sunset.

# Input : arr[] = {2, 3, 4, 5}
# Output : 4

def sunset_view(buildings):
    count = 1
    curr_max = buildings[0]
    for i in range(1,len(buildings)):
        if buildings[i] >= curr_max:
            count += 1
            curr_max = buildings[i]
    return count

print(sunset_view([7, 4, 8, 2, 9]))