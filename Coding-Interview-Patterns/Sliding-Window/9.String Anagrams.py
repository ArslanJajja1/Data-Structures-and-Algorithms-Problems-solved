# String Anagrams (hard) #
# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

def find_string_anagrams(String,Pattern):
    window_start = 0
    matched = 0
    result = []
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
        if window_end > len(Pattern)-1:
            left_char = String[window_start]
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
                window_start += 1
        if matched == len(char_frequency):
            result.append(window_start) 
    return result


print(find_string_anagrams("ppqp","pq"))
print(find_string_anagrams("abbcabc","abc"))

# Time Complexity : O(N+M)
# Space Complexity : O(K) or O(1) - Because the max chars could be 26 unique alphabest chars