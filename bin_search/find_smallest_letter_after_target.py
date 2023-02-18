# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (right + left) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if right < 0 or left >= len(letters): return letters[0]
        return letters[left]