# Find the corrupt pairs
def find_corrupt_pairs(arr):
    i = 0
    n = len(arr)
    ans = []
    while i < n:
        j = arr[i]-1
        if arr[i] != arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            i += 1
    for k in range(n):
        if arr[k] != k+1:
            ans = [arr[k],k+1]
    return ans


print(find_corrupt_pairs([3, 1, 2, 5, 2]))
print(find_corrupt_pairs([3, 1, 2, 3, 6, 4]))

# 1,2,3,2,5

# TC : O(N)
# SC : O(1)