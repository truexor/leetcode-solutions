class Solution:
    def maxDepth(self, s: str) -> int:
        nesting_depth = 0
        curr_depth = 0

        for ch in s:
            if ch == '(':
                curr_depth += 1
                nesting_depth = max(nesting_depth, curr_depth)

            elif ch == ')':
                curr_depth -= 1

            

        return nesting_depth