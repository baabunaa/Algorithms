# https://leetcode.com/problems/letter-case-permutation/description/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 1:
            if not s.isalpha(): return [s]
            return [s.upper(), s.lower()]
        ls, ans = self.letterCasePermutation(s[1:]), []
        for el in ls:
            el_1, el_2 = s[0].lower() + el, s[0].upper() + el
            ans.append(el_1)
            if el_1 != el_2: ans.append(el_2)
            
        return ans
