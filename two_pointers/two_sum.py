# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            b = target - nums[i]
            if nums[i] in seen:
                return [seen[nums[i]], i]
            seen[b] = i