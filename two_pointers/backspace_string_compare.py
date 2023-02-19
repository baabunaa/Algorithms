# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def get_real_str(s):
            index, count, res = len(s) - 1, 0, ""
            while index >= 0:
                if s[index] != "#" and count == 0:
                    res = s[index] + res
                elif s[index] != "#":
                    count -= 1
                else:
                    count += 1
                index -= 1
            return res
        
        return get_real_str(s) == get_real_str(t)