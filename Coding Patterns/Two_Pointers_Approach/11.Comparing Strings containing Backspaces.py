# Comparing Strings containing Backspaces (medium) #
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

def compare_strings(str1,str2):
    index1 = len(str1)-1
    index2 = len(str2)-1
    while index1 >=0 or index2 >= 0:
        i1 = get_next_valid_char(str1,index1)
        i2 = get_next_valid_char(str2,index2)
        if i1 == 0  and i2 == 0:
            return True
        if i1 == 0 or i2 == 0:
            return False
        if str1[i1] != str2[i2]:
            return False
        index1 = i1-1
        index2 = i2-1
    return True
def get_next_valid_char(s,index):
    backspaces = 0
    while index >= 0:
        if s[index] == "#":
            backspaces += 1
        elif backspaces > 0:
            backspaces -= 1
        else:
            break
        index -= 1
    return index



print(compare_strings("xy#z","xzz#"))
print(compare_strings("xy#z","xyz#"))
print(compare_strings("xp#","xyz##"))
print(compare_strings("xywrrmp","xywrrmu#p"))

# Time complexity #
# The time complexity of the above algorithm will be O(M+N) where ‘M’ and ‘N’ are the lengths of the two input strings respectively.

# Space complexity #
# The algorithm runs in constant space O(1).