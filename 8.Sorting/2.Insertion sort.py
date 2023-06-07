# Insertion Sort: Insertion sort builds the final sorted array one item at a time by repeatedly inserting a selected element into the right position of the already sorted part of the array. It has an average and worst-case time complexity of O(n^2).

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort([3,6,4,7,5,8,2]))