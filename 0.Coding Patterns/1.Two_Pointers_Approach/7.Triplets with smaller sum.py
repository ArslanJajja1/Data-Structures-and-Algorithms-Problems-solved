# Problem: Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case ?

def find_triplets(nums,target):
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left<right:
            current_sum = nums[i]+nums[left]+nums[right]
            if current_sum < target:
                for k in range(right,left,-1):
                    result.append([nums[i],nums[left],nums[k]])
                left += 1
            else:
                right -= 1
    return result

print(find_triplets([-1, 0, 2, 3],3 ))
print(find_triplets([-1, 4, 2, 1, 3],5 ))

# Time complexity #
# Sorting the array will take O(N∗logN). The searchPair(), in this case, will take O(N​2); the main while loop will run in O(N) but the nested for loop can also take O(N) - this will happen when the target sum is bigger than every triplet in the array.

# So, overall searchTriplets() will take O(N∗logN+N​3), which is asymptotically equivalent to (N​3).

# Space complexity #
# Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.