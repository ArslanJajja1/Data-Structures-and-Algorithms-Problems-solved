#include <iostream>
using namespace std;
#include <string>
#include <unordered_map>
/*
No-repeat Substring (hard)
Problem Statement #
Given a string, find the length of the longest substring which has no
repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is
"abc". Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" &
"cde".
  */
class NoRepeatingSubstring {
public:
  static int longestSubstring(const string& str) {
    int windowStart=0,maxLength=0,windowEnd;
    unordered_map<char,int> charTracking;
    for(windowEnd=0;windowEnd<str.length();windowEnd++){
      char rightChar = str[windowEnd];
       if(charTracking[rightChar]){
         windowStart = max(windowStart,charTracking[rightChar]+1);
      }
      charTracking[rightChar] = windowEnd;
      maxLength = max(maxLength,windowEnd-windowStart+1);
    }
    return maxLength;
    }
};
int main() {
  string str = "abbbb";
  int result = NoRepeatingSubstring::longestSubstring(str);
  cout << "Length of longest substring is : " << result << endl;
}
/*
Time Complexity #
The time complexity of the above algorithm will be O(N)O(N) where āNā is the number of characters in the input string.

Space Complexity #
The space complexity of the algorithm will be O(K)O(K) where KK is the number of distinct characters in the input string. This also means K<=NK<=N, because in the worst case, the whole string might not have any repeating character so the entire string will be added to the HashMap. Having said that, since we can expect a fixed set of characters in the input string (e.g., 26 for English letters), we can say that the algorithm runs in fixed space O(1)O(1); in this case, we can use a fixed-size array instead of the HashMap.


*/