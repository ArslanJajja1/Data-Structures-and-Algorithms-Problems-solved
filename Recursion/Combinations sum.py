# #* Combination Sum 1
def findCombinations(index, arr, ans, ds, target):
    if index == len(arr):
        if target == 0:
            ans.append(list(ds))
        return
    if arr[index] <= target:
        ds.append(arr[index])
        findCombinations(index, arr, ans, ds, target-arr[index])
        ds.pop()
    findCombinations(index+1, arr, ans, ds, target)


arr = [2, 3, 6, 7]
ans = []
findCombinations(0, arr, ans, [], 7)
print(ans)
