# Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

# Example 1:

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
# Example 2:

# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2

def remove_key(arr,key):
    j = 0
    for i in range(1,len(arr)):
        if arr[i] == key:
            continue
        if arr[j] == key:
            arr[i],arr[j] = arr[j],arr[i]
        j += 1
    return j

print(remove_key([3, 2, 3, 6, 3, 10, 9, 3],3))
print(remove_key([2, 11, 2, 2, 1],2))

# Time Complexity : O(N)
# Space Complexity : O(1)