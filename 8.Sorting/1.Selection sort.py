# Selection Sort: Selection sort works by repeatedly finding the minimum element from the unsorted part of the list and putting it at the beginning. It has an average and worst-case time complexity of O(n^2).

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx],arr[i] = arr[i],arr[min_idx]
    return arr

print(selection_sort([2,5,4,7,6,8,1]))