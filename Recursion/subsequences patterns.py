# #* Print subsequences whose sum is k
# def printS(i, arr, n, ds, k, sum):
#     if i >= n:
#         if sum == k:
#             print(ds)
#         return
#     ds.append(arr[i])
#     sum = sum + arr[i]
#     printS(i+1, arr, n, ds, k, sum)
#     ds.remove(arr[i])
#     sum = sum - arr[i]
#     printS(i+1, arr, n, ds, k, sum)


# arr = [1, 2, 1]
# printS(0, arr, len(arr), [], 2, 0)

# #* Print only 1 subsequence whose sum is k
def printS(i, arr, n, ds, k, sum):
    if i >= n:
        if sum == k:
            print(ds)
            return True
        return False
    ds.append(arr[i])
    sum = sum + arr[i]
    if printS(i+1, arr, n, ds, k, sum) == True:
        return True
    ds.remove(arr[i])
    sum = sum - arr[i]
    if printS(i+1, arr, n, ds, k, sum) == True:
        return True
    return False


arr = [1, 2, 1]
printS(0, arr, len(arr), [], 2, 0)
