# #* Combination Sum 1
# def findCombinations(index, arr, ans, ds, target):
#     if index == len(arr):
#         if target == 0:
#             ans.append(list(ds))
#         return
#     if arr[index] <= target:
#         ds.append(arr[index])
#         findCombinations(index, arr, ans, ds, target-arr[index])
#         ds.pop()
#     findCombinations(index+1, arr, ans, ds, target)


# arr = [2, 3, 6, 7]
# ans = []
# findCombinations(0, arr, ans, [], 7)
# print(ans)

# #* Combinations Sum 2
def findCombinations(index, arr, target, output, ds):
    if target == 0:
        output.append(list(ds))
        return
    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue
        if arr[i] > target:
            break
        ds.append(arr[i])
        findCombinations(i+1, arr, target-arr[i], output, ds)
        ds.pop()


arr = [10, 1, 2, 7, 6, 1, 5]
arr.sort()
target = 8
output = []
findCombinations(0, arr, target, output, [])
print(output)
