# 42. Trapping Rain Water
# Hard
# 25.8K
# 354
# Companies
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

def trapping_rain_water(arr):
    n = len(arr)
    left_max = [None]*n
    right_max = [None]*n
    water = [None]*n

    left_max[0] = arr[0]
    for i in range(1,n):
        if left_max[i-1] > arr[i]:
            left_max[i] = left_max[i-1]
        else:
            left_max[i] = arr[i]
    right_max[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        if right_max[i+1] > arr[i]:
            right_max[i] = right_max[i+1] 
        else:
            right_max[i] = arr[i]
    for i in range(n):
        water[i] = min(left_max[i],right_max[i]) - arr[i]
    return sum(water)

    
print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trapping_rain_water([4,2,0,3,2,5]))