# 30. Substring with Concatenation of All Words
# Hard
# 659
# 48
# Companies
# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.
# The output order does not matter. Returning [9,0] is fine too.
# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Explanation: Since words.length == 4 and words[i].length == 4, the concatenated substring has to be of length 16.
# There is no substring of length 16 is s that is equal to the concatenation of any permutation of words.
# We return an empty array.
# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
# Explanation: Since words.length == 3 and words[i].length == 3, the concatenated substring has to be of length 9.
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"] which is a permutation of words.
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"] which is a permutation of words.
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"] which is a permutation of words.
 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not len(words):
           return []
        words_freq = {}
        word_length = len(words[0])
        words_count = len(words)
        total_length = word_length * words_count
        result = []
        for word in words:
            if word not in words_freq:
                words_freq[word] = 0
            words_freq[word] += 1
        for i in range(len(s)-total_length+1):
            words_seen = {}
            for j in range(0,words_count):
                next_word_index = i+j*word_length
                word = s[next_word_index:next_word_index+word_length]
                if word not in words_freq:
                    break
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1
                if words_seen[word] > words_freq.get(word,0):
                    break
                if j+1 == words_count:
                    result.append(i)
        return result


# Time Complexity #
# The time complexity of the above algorithm will be O(N∗M∗Len) where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.

# Space Complexity #
# The space complexity of the algorithm is O(M) since at most, we will be storing all the words in the two HashMaps. In the worst case, we also O(N) space for the resulting list. So, the overall space complexity of the algorithm will be O(M+N).







