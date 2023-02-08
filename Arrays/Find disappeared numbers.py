# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            el = nums[abs(abs(nums[i])-1)]
            if el >= 0:
                nums[abs(abs(nums[i])-1)] *= -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                res.append(i+1) 
        return res
