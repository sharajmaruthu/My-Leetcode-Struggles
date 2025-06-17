from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s: str, left: int, right: int, res: List[str]):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right, res)
            if right < left:
                backtrack(s + ')', left, right + 1, res)
        
        result = []
        backtrack("", 0, 0, result)
        return result
