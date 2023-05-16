# Find the First K Missing Positive Numbers (hard) #
# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

# Example 1:

# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Example 2:

# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
# Example 3:

# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.


def find_k_missing_numbers(nums,k):
    missing_nums = []
    num_set = set(nums)
    last = max(num_set)
    for i in range(1,k+1):
        if i not in num_set:
            missing_nums.append(i)
    while len(missing_nums) < k:
        last += 1
        if last not in num_set:
            missing_nums.append(last)
    return missing_nums

print(find_k_missing_numbers([3, -1, 4, 5, 5],3))
print(find_k_missing_numbers([2, 3, 4],3))
print(find_k_missing_numbers([-2, -3, 4],2))

# TC : O(N)
# SC : O(N)