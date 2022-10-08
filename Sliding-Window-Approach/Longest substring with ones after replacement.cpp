/* Problem Statement #
Given an array containing 0s and 1s, if you are allowed to replace no more than
‘k’ 0s with 1s, find the length of the longest contiguous subarray having all
1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous
subarray of 1s having length 6. Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest
contiguous subarray of 1s having length 9.*/
#include <iostream>
using namespace std;
#include <vector>

class LongestSubstring {
public:
  static int lengthOfLongestSubstring(int k, const vector<int> &nums) {
    int windowStart = 0, maxLength = 0, zerosLength = 0, windowEnd;
    for (windowEnd = 0; windowEnd < nums.size(); windowEnd++) {
      int rightNum = nums[windowEnd];
      if (rightNum == 0) {
        zerosLength++;
      }
      if (zerosLength > k) {
        if (nums[windowStart] == 0)
          zerosLength--;
        windowStart++;
      }
      maxLength = max(maxLength, windowEnd - windowStart + 1);
    }
    return maxLength;
  }
};
int main() {
  vector<int> nums = {0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1};
  int k = 3;
  vector<int> arr = {0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1};
  int result1 = LongestSubstring::lengthOfLongestSubstring(k, nums);
  int result2 = LongestSubstring::lengthOfLongestSubstring(2, arr);
  cout << "Longest subarray 1 : " << result1 << endl;
  cout << "Longest subarray 2 : " << result2 << endl;
}
/*
Time Complexity #
The time complexity of the above algorithm will be O(N)  where ‘N’ is the count
of numbers in the input array.

Space Complexity #
The algorithm runs in constant space O(1).
*/