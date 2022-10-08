/*
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
*/
#include <iostream>
using namespace std;
#include <string>
#include <unordered_map>
#include <vector>

class StringAnagrams {
public:
  static vector<int> findAnagrams(const string &str, const string &pattern) {
    int windowStart, windowEnd, matched = 0;
    unordered_map<char, int> hashmap;
    vector<int> resultArray;
    for (char ch : pattern)
      hashmap[ch]++;
    for (windowEnd = 0; windowEnd < str.length(); windowEnd++) {
      char rightChar = str[windowEnd];
      if (hashmap.find(rightChar) != hashmap.end()) {
        hashmap[rightChar]--;
        if (hashmap[rightChar] == 0)
          matched++;
      }
      if (matched == (int)hashmap.size()) {
        resultArray.push_back(windowStart);
      }
      if (windowEnd >= pattern.length() - 1) {
        char leftChar = str[windowStart++];
        if (hashmap.find(leftChar) != hashmap.end()) {
          if (hashmap[leftChar] == 0) {
            matched--;
          }
          hashmap[leftChar]++;
        }
      }
    }
    return resultArray;
  }
};
int main() {
  // auto result = StringAnagrams::findAnagrams("ppqp", "pq");
  // for (auto ch : result)
  //   cout << " " << ch << " " << endl;
  auto result1 = StringAnagrams::findAnagrams("abbcabc", "abc");
  for (auto ch : result1)
    cout << " " << ch << " ";
}

/*
Time Complexity #
The time complexity of the above algorithm will be O(N + M)  where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity #
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap. In the worst case, we also need O(N) space for the result list, this will happen when the pattern has only one character and the string contains only that character.
*/