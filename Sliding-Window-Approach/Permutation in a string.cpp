/*
Permutation in a String (hard) #
Given a string and a pattern, find out if the string contains any permutation of
the pattern.

Permutation is defined as the re-arranging of the characters of the string. For
example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given
pattern. Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a
substring. Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given
pattern.
*/
#include <iostream>
using namespace std;
#include <string>
#include <unordered_map>

class Permutation {
public:
  static bool containsPermutation(const string &pattern,
                                  const string &characters) {
    unordered_map<char, int> hashmap;
    for (auto ch : pattern) {
      hashmap[ch]++;
    }
    int windowStart, windowEnd, matched = 0;
    for (windowEnd = 0; windowEnd < characters.length(); windowEnd++) {
      char rightChar = characters[windowEnd];
      if (hashmap.find(rightChar) != hashmap.end()) {
        hashmap[rightChar]--;
        if (hashmap[rightChar] == 0) {
          matched++;
        }
      }

      if (matched == (int)hashmap.size()) {
        return true;
      }
      if (windowEnd >= pattern.length() - 1) {
        char leftChar = characters[windowStart++];
        if (hashmap.find(leftChar) != hashmap.end()) {
          if (hashmap[leftChar] == 0) {
            matched--;
          }
          hashmap[leftChar]++;
        }
      }
    }
    return false;
  }
};

int main() {

  string characters = "oidbcaf";
  string pattern = "abc";
  string characters1 = "odicf";
  string pattern1 = "dc";
  string characters2 = "bcdxabcdy";
  string pattern2 = "bcdyabcdx";
  string characters3 = "aaacb";
  string pattern3 = "abc";
  int result = Permutation::containsPermutation(pattern, characters);
  int result1 = Permutation::containsPermutation(pattern1, characters1);
  int result2 = Permutation::containsPermutation(pattern2, characters2);
  int result3 = Permutation::containsPermutation(pattern3, characters3);
  cout << "Contains Permutation : " << result << endl;
  cout << "Contains Permutation 1 : " << result1 << endl;
  cout << "Contains Permutation 2 : " << result2 << endl;
  cout << "Contains Permutation 3 : " << result3 << endl;
}
/*
Time Complexity #
The time complexity of the above algorithm will be O(N + M) where ‘N’ and ‘M’ are the number of characters in the input string and the pattern respectively.

Space Complexity #
The space complexity of the algorithm is O(M) since in the worst case, the whole pattern can have distinct characters which will go into the HashMap.
*/