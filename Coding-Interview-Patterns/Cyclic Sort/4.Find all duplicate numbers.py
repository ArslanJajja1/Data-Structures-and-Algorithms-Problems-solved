# Problem Statement #
# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some duplicates, find all the duplicate numbers without using any extra space.

# Example 1:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:

# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]

def find_all_duplicates(arr):
    i = 0
    while i < len(arr):
        j = arr[i]-1
        if arr[i] != arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            i += 1
    print(arr)
    duplicate_numbers = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            duplicate_numbers.append(arr[i])
    return duplicate_numbers

print(find_all_duplicates([3, 4, 4, 5, 5]))
print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
