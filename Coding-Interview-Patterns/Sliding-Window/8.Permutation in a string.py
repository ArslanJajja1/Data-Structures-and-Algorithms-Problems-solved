# Permutation in a String (hard) #
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have 
# �
# !
# n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

def find_permutation(String,Pattern):
    char_frequency = {}
    window_start = 0
    matched = 0
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
        if matched == len(char_frequency):
            return True
        if window_end >= len(Pattern)-1:
            left_char = String[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
            window_start += 1
    return False

print(find_permutation("oidbcaf","abc"))
print(find_permutation("odicf","dc"))
print(find_permutation("bcdxabcdy","bcdyabcdx"))
print(find_permutation("aaacb","abc"))

# Time Complexity : O(N+M)
# Space Complexity : O(M)

