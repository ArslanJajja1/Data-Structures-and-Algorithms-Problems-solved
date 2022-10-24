def reverseArray(i, arr, n):
    if i >= n/2:
        return
    temp = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = temp
    return reverseArray(i+1, arr, n)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverseArray(0, arr, len(arr))
print('Reversed Array : ', arr)
