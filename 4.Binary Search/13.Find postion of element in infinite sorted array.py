# Find the position of an element in infinite sorted array

def find_element_positon(nums,target):
    start = 0
    end = 1
    while nums[end] < target:
        start = end
        end *= 2
    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1

print(find_element_positon([1,2,3,5,7,8,9,10,11,12,'........'],12))

# SC : O(1)
# TC : O(logn)