# Problem Statement #
# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".

def find_no_repeat_substring(String):
    window_start = 0
    hashmap = {}
    longest_substring = 0
    for window_end in range(len(String)):
        while String[window_end] in hashmap:
            del hashmap[String[window_start]]
            window_start += 1
        if String[window_end] not in hashmap:
            hashmap[String[window_end]] = window_end
        longest_substring = max(longest_substring,window_end-window_start+1)
    return longest_substring


print(find_no_repeat_substring("aabccbb"))
print(find_no_repeat_substring("abbbb"))
print(find_no_repeat_substring("abccde"))

# Time Complexity : O(N)
# Space Complexity : O(N)

