# Find the Smallest Missing Positive Number (medium) #
# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Example 1:

# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:

# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:

# Input: [3, 2, 5, 1]
# Output: 4

def find_smallest_missing_positive(arr):
    i = 0
    while i < len(arr):
        j = arr[i]-1
        if j >= 0 and j < len(arr) and arr[i] != arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            i += 1
    print(arr)
    for i in range(len(arr)):
        if arr[i] != i+1:
            return i+1

print(find_smallest_missing_positive([-3, 1, 5, 4, 2]))
print(find_smallest_missing_positive([3, -2, 0, 1, 2]))
print(find_smallest_missing_positive([3, 2, 5, 1]))
