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

# ⁡⁢⁣⁣Time Complexity⁡ : ⁡⁣⁢⁣The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.⁡

# ⁡⁢⁣⁣Space Complexity⁡ : ⁡⁣⁢⁣The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need (N) space for the resulting substring, which will happen when the input string is a permutation of the pattern.⁡
