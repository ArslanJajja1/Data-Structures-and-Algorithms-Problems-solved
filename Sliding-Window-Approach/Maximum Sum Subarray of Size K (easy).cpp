#include <iostream>
using namespace std;
#include <vector>
// Maximum Sum Subarray of Size K (easy)
/*Given an array of positive numbers and a positive number ‘k’, find the maximum
sum of any contiguous subarray of size ‘k’. Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

*/
int maximum_sum(int k, vector<int> &arr)
{
  int windowSum = 0;
  int windowStart = 0;
  int maximumSum = 0;
  int windowEnd;
  for (windowEnd = 0; windowEnd < arr.size(); windowEnd++)
  {
    windowSum += arr[windowEnd];
    if (windowEnd >= k)
    {
      windowSum -= arr[windowStart];
      windowStart++;
    }
    maximumSum = max(windowSum, maximumSum);
  }
  return maximumSum;
};
int main()
{
  vector<int> arr = {2, 1, 5, 1, 3, 2};
  vector<int> arr2 = {2, 3, 4, 1, 5};
  int k = 3;
  int result1 = maximum_sum(k, arr);
  cout << "Result 1 => " << result1 << endl;
  int result2 = maximum_sum(2, arr2);
  cout << "Result 2 => " << result2;
}

/*
 Time Complexity O(n)
 Space Complexity O(1)

Time Complexity #
The time complexity of the above algorithm will be O(N)O(N).

Space Complexity #
The algorithm runs in constant space O(1)O(1).
 */