# ​‌‍‌⁡⁣⁣⁢Problem Statement ⁡​
# ⁡⁢⁣⁣Given a string, find the length of the longest substring in it with no more than K distinct characters.⁡

# ⁡⁢⁣⁣Example 1:⁡

# ⁡⁣⁢⁣Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# ⁡⁢⁣⁣Example 2:⁡⁡

# ⁡⁣⁢⁣Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".⁡

# ⁡⁢⁣⁣Example 3:⁡

# ⁡⁣⁢⁣Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".⁡

# ⁡⁣⁣⁢Optimized way⁡ :
import math


def longest_substr(s, k):
    maxLength = -math.inf
    windowStart = 0
    hashmap = {}
    for windowEnd in range(len(s)):
        char = s[windowEnd]
        if char not in hashmap:
            hashmap[char] = 0
        hashmap[char] += 1
        while len(hashmap) > k:
            leftChar = s[windowStart]
            hashmap[leftChar] -= 1
            if hashmap[leftChar] == 0:
                del hashmap[leftChar]
            windowStart += 1
        maxLength = max(maxLength, windowEnd-windowStart+1)

    return maxLength


print(longest_substr("araaci", 2))
print(longest_substr("araaci", 1))
print(longest_substr("cbbebi", 3))

# ⁡⁣⁣⁢⁡⁢⁣⁣Time Complexity⁡ ⁡:  ⁡⁣⁢⁣The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).⁡

# ⁡⁢⁣⁣Space Complexity ⁡⁡: ⁡⁣⁢⁣The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.⁡
