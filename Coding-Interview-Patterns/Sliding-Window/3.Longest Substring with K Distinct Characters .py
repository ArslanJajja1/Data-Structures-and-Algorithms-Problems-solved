# Longest Substring with K Distinct Characters (medium)

# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def find_longest_substring(s,k):
    window_start = 0 
    longest_substring = 0
    hashmap = {}
    for window_end in range(len(s)):
        if s[window_end] not in hashmap:
            hashmap[s[window_end]] = 0
        hashmap[s[window_end]] += 1
        while len(hashmap) > k:
            hashmap[s[window_start]] -= 1
            if hashmap[s[window_start]] == 0:
                del hashmap[s[window_start]]
            window_start += 1
        longest_substring = max(longest_substring,window_end-window_start+1)
    return longest_substring

print(find_longest_substring("araaci",2))
print(find_longest_substring("araaci",1))
print(find_longest_substring("cbbebi",3))

# Time Complexity : O(N)
# Space Complexity : O(K)
