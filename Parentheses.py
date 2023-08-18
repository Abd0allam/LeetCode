class Solution:
    def generateParenthesis(self, n: int):
        def rec_generate(open, close, s):
             # s==>the current combination of parentheses
            if len(s) == n * 2:  # n*2 = () *n
                res.append(s)
                return 

            if open < n:
                rec_generate(open + 1, close, s + '(')

            if close < open:
                rec_generate(open, close + 1, s + ')')

        res = []
        rec_generate(0, 0, '')
        return res

n = 3
o=Solution().generateParenthesis(n)

print(o)
