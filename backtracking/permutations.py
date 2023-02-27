# https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return [nums]
        p_res, ans = self.permute(nums[1:]), []
        for p in p_res:
            for i in range(len(p)+1):
                ans.append(p[:i]+[nums[0]]+p[i:])
        return ans
    