# Problem Statement #
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.

def triplet_sum(arr):
    arr.sort()
    res = []
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left < right:
            sum_of_triplet = arr[i] + arr[left] + arr[right]
            if sum_of_triplet < 0 :
                left += 1
            elif sum_of_triplet > 0:
                right -= 1
            else:
                res.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
    return res

print(triplet_sum([-3, 0, 1, 2, -1, 1, -2]))
print(triplet_sum([-5, 2, -1, -2, 3]))

# Time Complexity: O(NLOGN+N^2)
# Space Complexity: O(N)