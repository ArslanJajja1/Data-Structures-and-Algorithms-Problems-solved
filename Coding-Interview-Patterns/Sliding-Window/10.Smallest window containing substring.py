# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:

# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.

def find_smallest_window(String,Pattern):
    window_start = 0
    substring_start = 0
    matched = 0
    substring_length = len(String)+1
    char_frequency = {}
    for char in Pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    for window_end in range(len(String)):
        right_char = String[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        while matched == len(char_frequency):
            if substring_length > window_end-window_start+1:
                substring_length = window_end-window_start+1
                substring_start = window_start
            left_char = String[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            window_start += 1
    print(substring_start,substring_length)
    if substring_length == len(String)+1:
        return ""
    return String[substring_start:substring_start+substring_length]

print('1',find_smallest_window("aabdec","abc"))
print('2',find_smallest_window("abdabca","abc"))
print('3',find_smallest_window("adcad","abc"))

# Time Complexity : O(N)
# Space Complexity : O(K)