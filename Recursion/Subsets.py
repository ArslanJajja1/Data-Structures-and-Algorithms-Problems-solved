# #* Subset 1
# def subset1(index, sum, arr, n, sumset):
#     if index == n:
#         sumset.append(sum)
#         return
#     subset1(index+1, sum+arr[index], arr, n, sumset)
#     subset1(index+1, sum, arr, n, sumset)


# arr = [3, 1, 2]
# sumset = []
# subset1(0, 0, arr, len(arr), sumset)
# sumset.sort()
# print(sumset)

# #* Subset 2
def subset2(index, arr, ds, ans):
    ans.append(list(ds))
    for i in range(index, len(arr)):
        if i != index and arr[i-1] == arr[i]:
            continue
        ds.append(arr[i])
        subset2(index+1, arr, ds, ans)
        ds.pop()


arr = [0]
ds = []
ans = []
arr.sort()
subset2(0, arr, ds, ans)
print(ans)
