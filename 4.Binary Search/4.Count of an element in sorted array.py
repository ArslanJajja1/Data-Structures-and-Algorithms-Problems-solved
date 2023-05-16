# Count of an element in sorted array
def count_element(arr,target):
    first_occurence = find_first_occurence(arr,target)
    last_occurence = find_last_occurence(arr,target)
    if first_occurence == -1 and last_occurence == -1:
        return -1
    if first_occurence == -1 or last_occurence == -1:
        return 1
    count = last_occurence - first_occurence + 1
    return count
def find_first_occurence(arr,target):
    start = 0
    end = len(arr)-1
    result = -1
    while start <= end:
        mid = start + (end-start)//2
        if target == arr[mid]:
            result = mid
            end = mid - 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result
            
def find_last_occurence(arr,target):
    start = 0
    end = len(arr)-1
    result = -1
    while start <= end:
        mid = start + (end-start)//2
        if target == arr[mid]:
            result = mid
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return result

print(count_element([1,2,3,4,4,4,4,5,7,8,9],4))
print(count_element([1,2,3,4,5,7,8,9],6))
print(count_element([1,2,3,4,5,7,8,9],7))

# SC : O(1)
# TC : O(n)
