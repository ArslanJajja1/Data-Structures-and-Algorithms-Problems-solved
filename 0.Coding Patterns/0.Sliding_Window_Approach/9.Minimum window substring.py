# ​‌‍‌⁡⁣⁣⁢Smallest Window containing Substring

# ⁡⁣⁢⁣​Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.⁡

# ⁡⁣⁣⁢Example 1:
# ⁡
# ⁡⁣⁢⁣Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"⁡

# ⁡⁣⁣⁢Example 2:
# ⁡
# ⁡⁣⁢⁣Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".⁡

# ⁡⁣⁣⁢Example 3:
# ⁡
# ⁡⁣⁢⁣Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.⁡


def minWindow(s: str, t: str) -> str:
    window_start = 0
    substr_start = 0
    min_length = len(s)+1
    matched = 0
    hashmap = {}
    for char in t:
        if char not in hashmap:
            hashmap[char] = 0
        hashmap[char] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in hashmap:
            hashmap[right_char] -= 1
            if hashmap[right_char] == 0:
                matched += 1
        while matched == len(hashmap):
            if min_length > window_end-window_start+1:
                min_length = window_end-window_start+1
                substr_start = window_start
            left_char = s[window_start]
            window_start += 1
            if left_char in hashmap:
                if hashmap[left_char] == 0:
                    matched -= 1
                hashmap[left_char] += 1
    if min_length > len(s):
        return ""
    else:
        return s[substr_start:substr_start+min_length]


print(minWindow("aabdec", "abc"))
print(minWindow("abdabca", "abc"))
print(minWindow("adcad", "abc"))


# ⁡⁢⁣⁣Time Complexity⁡ : ⁡⁣⁢⁣The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.⁡

# ⁡⁢⁣⁣Space Complexity⁡ : ⁡⁣⁢⁣The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need (N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.⁡
