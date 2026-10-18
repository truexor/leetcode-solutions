class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        counter = 0

        for ch in s:
            if ch == '(':
                counter += 1
                if counter > 1:
                    ans += ch

            elif ch == ')':
                counter -= 1
                if counter > 0:
                    ans += ch


        return ans