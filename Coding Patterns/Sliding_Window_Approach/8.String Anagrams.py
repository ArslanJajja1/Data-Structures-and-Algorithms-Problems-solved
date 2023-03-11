# ​‌‍‌⁡⁣⁣⁢String Anagrams
# ⁡​
# ⁡⁣⁢⁣Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.⁡

# ⁡⁣⁣⁢Example 1:
# ⁡
# ⁡⁣⁢⁣Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".⁡

# ⁡⁣⁣⁢Example 2:
# ⁡
# ⁡⁣⁢⁣Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".⁡
def findAnagrams(s: str, p: str):
    window_start = 0
    matched = 0
    count = {}
    result = []
    for char in p:
        if char not in count:
            count[char] = 0
        count[char] += 1
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in count:
            count[right_char] -= 1
            if count[right_char] == 0:
                matched += 1
        if matched == len(count):
            result.append(window_start)
        if window_end >= len(p)-1:
            left_char = s[window_start]
            window_start += 1
            if left_char in count:
                if count[left_char] == 0:
                    matched -= 1
                count[left_char] += 1
    return result


print(findAnagrams("ppqp", "pq"))
print(findAnagrams("abbcabc", "abc"))
