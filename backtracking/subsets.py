# https://leetcode.com/problems/subsets/description/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = self.subsets(nums[1:])
        return res + [[nums[0]] + el for el in res]