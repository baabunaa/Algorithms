# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b