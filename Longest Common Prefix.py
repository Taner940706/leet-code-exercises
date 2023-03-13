# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        # maximum = 999

        for i in range(len(min(strs, key=len))):
            new_list = [item[i] for item in strs]
            if [new_list[0]] * len(new_list) == new_list:
                prefix = prefix + new_list[0]
            else:
                break

        if len(prefix) > 0:
            return prefix
        else:
            return ""
