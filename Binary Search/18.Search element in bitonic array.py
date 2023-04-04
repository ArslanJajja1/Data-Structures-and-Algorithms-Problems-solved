# Search an element in bitonic array

def search_element(nums,target):
    n = len(nums)
    if n == 0 or nums is None: return -1
    if n == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    peak_element = find_peak(nums)
    left = binary_search_asc(nums,target,0,peak_element)
    right = binary_search_desc(nums,target,peak_element,n-1)
    
    if left == -1 and right == -1: return -1
    if left == -1: return right
    if right == -1: return left


# Find peak element
def find_peak(nums):
    n = len(nums)
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if mid > 0 and mid < n-1:
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if mid == 0:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return mid+1
            if mid == n-1:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid-1

# Binary search in asc sorted array
def binary_search_asc(nums,target,start,end):
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
# Binary search in desc sorted array
def binary_search_desc(nums,target,start,end):
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            end = mid - 1
        else:
            start = mid + 1
    return -1


print(search_element([1,3,4,6,5,2,0],0))
print(search_element([1,3,4,6,5,2,0],7))
print(search_element([],7))
print(search_element([1],7))
print(search_element([7],7))


# SC : O(1)
# TC : O(logn)