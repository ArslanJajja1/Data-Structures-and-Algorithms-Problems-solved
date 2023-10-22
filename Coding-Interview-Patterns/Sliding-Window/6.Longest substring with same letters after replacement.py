# Problem Statement #
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

def find_longest_substring(String,k):
    window_start = 0
    frequency = {}
    longest_substring = 0
    max_char = 0
    for window_end in range(len(String)):
        right_char = String[window_end]
        if right_char not in frequency:
            frequency[right_char] = 0
        frequency[right_char] += 1
        max_char = max(max_char,frequency[right_char])
        while ((window_end-window_start+1) - max_char) > k:
            left_char = String[window_start]
            frequency[left_char] -= 1
            if frequency[left_char] == 0:
                del frequency[left_char]
            window_start += 1
        longest_substring = max(longest_substring,window_end-window_start+1)
    return longest_substring



print(find_longest_substring("aabccbb",2))
print(find_longest_substring("abbcb",1))
print(find_longest_substring("abccde",1))

# Time Complexity : O(N)
# Space Complexity :O(N)/O(1)
