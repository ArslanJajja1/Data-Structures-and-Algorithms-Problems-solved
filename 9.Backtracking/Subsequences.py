
# #* All subsequences of an array
def subsequences(i, arr, ds, n):
    if i >= n:

        for i in ds:
            print(i, end=' ')
        print('\n')
        if len(ds) == 0:
            print('{}')

        return
    ds.append(arr[i])
    subsequences(i+1, arr, ds, n)
    ds.remove(arr[i])
    subsequences(i+1, arr, ds, n)


arr = [3, 1, 2]
subsequences(0, arr, [], len(arr))
