# Given a sorted array arr[] of size N, some elements of array are moved to either of the adjacent positions, i.e., arr[i] may be present at arr[i+1] or arr[i-1] i.e. arr[i] can only be swapped with either arr[i+1] or arr[i-1]. The task is to search for an element in this array.

# Examples : 

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
# Output: 2 
# Explanation: Output is index of 40 in given array i.e. 2

# Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
# Output: -1
# Explanation: -1 is returned to indicate the element is not present

def nearly_sorted_array(nums,key):
    n = len(nums)
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == key:
            return mid
        if mid > 0 and nums[mid-1] == key:
            return mid-1
        if mid < n-1 and nums[mid+1] == key:
            return mid+1
        if key < nums[mid]:
            end = mid - 2
        if key > nums[mid]:
            start = mid + 2
    return -1

print(nearly_sorted_array([10, 3, 40, 20, 50, 80, 70],40))
print(nearly_sorted_array([10, 3, 40, 20, 50, 60, 70],90))
print(nearly_sorted_array([1,2,3,4,6,5,8,7],3))


# SC : O(1)
# TC : O(logn)