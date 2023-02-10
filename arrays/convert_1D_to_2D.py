# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        res = []
        for i in range(0,len(original),n):
            res.append(original[i:i+n])
        return res