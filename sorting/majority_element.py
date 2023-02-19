# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 0
        for n in nums[1:]:
            if n == major:
                count += 1
            elif n != major and count > 0:
                count -= 1
            else:
                major = n
                count = 0
        return major
