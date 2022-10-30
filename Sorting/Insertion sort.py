def insertion_sort(arr):
    for i in range(len(arr)):
        j = i-1
        while j >= 0 and arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp
            j = j-1


arr = [5, 4, 3, 2, 1]
insertion_sort(arr)
print('Sorted array with insertion sort : ', arr)
