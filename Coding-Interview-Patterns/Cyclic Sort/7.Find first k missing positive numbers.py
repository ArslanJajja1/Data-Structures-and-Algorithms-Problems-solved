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

def find_first_k_missing_positive(arr,k):
    i = 0
    while i < len(arr):
        j = arr[i]-1
        if  arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            i += 1
    print(arr) 
    missing_numbers = []
    extra_numbers = set()
    for i in range(len(arr)):
        if len(missing_numbers) < k:
            if arr[i] != i+1:
                missing_numbers.append(i+1)
                extra_numbers.add(arr[i])
    i = 1
    n = len(arr)
    while len(missing_numbers) < k:
        candidate_number = i+n
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        i += 1
    return missing_numbers
    


print(find_first_k_missing_positive([3, -1, 4, 5, 5],3))
print(find_first_k_missing_positive([2, 3, 4],3))
print(find_first_k_missing_positive([-2, -3, 4],2))

