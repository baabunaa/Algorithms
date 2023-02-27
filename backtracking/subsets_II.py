# https://leetcode.com/problems/subsets-ii/description/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def helper(nums, seen):
            if len(nums) == 0: return [[]]
            res = helper(nums[1:], seen)
            for el in res.copy():
                new_el = nums[:1] + el
                if str(new_el) not in seen:
                    res.append(new_el)
                    seen.add(str(new_el))
            return res

        return helper(nums,set())