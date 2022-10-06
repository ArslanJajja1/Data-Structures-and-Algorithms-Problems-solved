#include <iostream>
using namespace std;
#include <limits>
#include <vector>
// Smallest Subarray with a given sum (easy)

/*Problem Statement #
Given an array of positive numbers and a positive number ‘S’, find the length of
the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
Return 0, if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5,
2]. Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is
[8]. Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3,
4, 1] or [1, 1, 6].

*/
class LengthOfSubArray {
public:
  static int findSmallestSubarray(int s, const vector<int> &arr) {
    int windowStart = 0;
    int minimumLength = numeric_limits<int>::max();
    int windowSum = 0;
    int windowEnd;
    for (windowEnd = 0; windowEnd < arr.size(); windowEnd++) {
      windowSum += arr[windowEnd];
      while (windowSum >= s) {
        minimumLength = min(minimumLength, windowEnd - windowStart + 1);
        windowSum -= arr[windowStart];
        windowStart++;
      }
    }
    return minimumLength == numeric_limits<int>::max() ? 0 : minimumLength;
  }
};
int main() {
  vector<int> nums = {3, 4, 1, 1, 6};
  int S = 8;
  int result = LengthOfSubArray::findSmallestSubarray(S, nums);
  cout << "Smallest subarray with given sum : " << result << endl;
}
/*
Time complexity : O(n)
Space complexity : O(1)

Time Complexity #
The time complexity of the above algorithm will be O(N). The outer for loop runs
for all elements and the inner while loop processes each element only once,
therefore the time complexity of the algorithm will be O(N+N) which is
asymptotically equivalent to O(N).

Space Complexity #
The algorithm runs in constant space O(1).
*/