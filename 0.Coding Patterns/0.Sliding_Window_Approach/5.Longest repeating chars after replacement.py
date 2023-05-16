# ​‌‍‌⁡⁣⁣⁢424. Longest Repeating Character Replacement⁡​

# ⁡⁣⁢⁣You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.⁡

# ⁡⁣⁣⁢Example 1:
# ⁡⁣⁢⁣
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.⁡

# ⁡⁣⁣⁢Example 2:⁡

# ⁡⁣⁢⁣Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.⁡


# ⁡⁣⁣⁢Constraints:⁡
# ⁡⁣⁢⁣
# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length⁡

import math


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = 0
        max_length = -math.inf
        count = {}

        for window_end in range(len(s)):
            count[s[window_end]] = 1 + count.get(s[window_end], 0)
            while (window_end-window_start+1) - max(count.values()) > k:
                left_char = s[window_start]
                count[left_char] -= 1
                if count[left_char] == 0:
                    del count[left_char]
                window_start += 1
            max_length = max(max_length, window_end-window_start+1)
        return max_length

# ⁡⁣⁣⁢Time complexity ⁡: ⁡⁣⁢⁣The time complexity for this algorithm will be O(26.n) which is 0(n) because we are looping through each characters atmost once and then we are checking count hashmap for the current maximum value in the hashmap which will be O(26) constant time operation because there are 26 uppercase characters ;

# ⁡⁣⁣⁢Space complexity ⁡: ⁡⁣⁢⁣The space complexity for above algorithm will be 0(k) because in count hashmap as we are storing max k chars in count hashmap ;⁡
