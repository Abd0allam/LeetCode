# class Solution:
#     def generateParenthesis(self, n: int):
#         if n == 0:
#             return []
        
#         results = []
#         self.generate('', n, n, results)
#         return results
    
#     def generate(self, s, open, close, results):
#         if open == 0 and close == 0:
#             # s==>the current combination of parentheses , open (the number of remaining opening parentheses), close (the number of remaining closing parentheses), and results (the list to store the generated combinations).
#             results.append(s)
#             return
        
#         if open > 0:
#             self.generate(s + '(', open - 1, close, results)
        
#         if close > open:
#             self.generate(s + ')', open, close - 1, results)
    
class Solution:
    def generateParenthesis(self, n: int):
        def dfs(open, close, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if open < n:
                dfs(open + 1, close, s + '(')

            if close < open:
                dfs(open, close + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

n = 3
o=Solution().generateParenthesis(n)

print(o)