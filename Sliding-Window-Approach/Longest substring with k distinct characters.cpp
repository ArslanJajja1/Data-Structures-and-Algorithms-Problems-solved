#include <iostream>
using namespace std;
#include <limits>
#include <string>
#include <unordered_map>
#include <vector>

// Longest Substring with K Distinct Characters (medium)

/*Problem Statement #
Given a string, find the length of the longest substring in it with no more than
K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is
"araa". Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is
"aa". Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters
are "cbbeb" & "bbebi"..
 */
class LongestSubstringWithKDistinctCharacters {
public:
  static int longestSubstr(int k, const string &str) {
    unordered_map<char, int> charFrequencyMap;
    int maxLength = 0, windowStart = 0, windowEnd;
    string maxString;
    for (windowEnd = 0; windowEnd < str.length(); windowEnd++) {
      char rightChar = str[windowEnd];
      charFrequencyMap[rightChar++];
      while ((int)charFrequencyMap.size() > k) {
        char leftChar = str[windowStart];
        charFrequencyMap[leftChar--];
        if (charFrequencyMap[leftChar] == 0) {
          charFrequencyMap.erase(leftChar);
        }
        windowStart++;
      }
      maxLength = max(maxLength, windowEnd - windowStart + 1);
      maxString = max(maxString,str.substr(windowStart,windowEnd-windowStart+1));
      cout<<"Max string is = "<<maxString<<endl;
    }
    return maxLength;
  };
};
int main() {
  int result =
      LongestSubstringWithKDistinctCharacters::longestSubstr(3, "cbbeb");
  cout << "Result : " << result << endl;
}
/*
Time Complexity #
The time complexity of the above algorithm will be O(N)O(N) where ‘N’ is the number of characters in the input string. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N)O(N+N) which is asymptotically equivalent to O(N)O(N).

Space Complexity #
The space complexity of the algorithm is O(K)O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.
*/