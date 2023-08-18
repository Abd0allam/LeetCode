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

# The function generateParenthesis takes an integer n as input.

# An inner recursive function called rec_generate. This function takes three parameters: open (the count of open parentheses), close (the count of closed parentheses), and s (the current combination of parentheses).

# Inside the rec_generate function, the code checks if the length of s is equal to n * 2. This condition represents the base case where s has reached the desired length, which is n * 2 because each valid combination of parentheses will have n pairs.

# If the base case is met, it means that a valid combination has been generated, so s is appended to the res list, which stores all the valid combinations. Then, the function returns.

# If the base case is not met, the code proceeds to the recursive steps. If the count of open parentheses (open) is less than n, it means that more open parentheses can be added to the current combination. In this case, the function calls itself recursively with open + 1, close, and s + '(' as the new parameters. This represents adding an open parenthesis to the current combination.

# If the count of closed parentheses (close) is less than open, it means that more closed parentheses can be added to the current combination. In this case, the function calls itself recursively with open, close + 1, and s + ')' as the new parameters. This represents adding a closed parenthesis to the current combination.

# The initial call to the rec_generate function is made with the initial values of open (0), close (0), and an empty string s.

# After the recursive function finishes, the res list contains all the valid combinations of parentheses. It is then returned as the final result.

# The algorithm used in this code is a backtracking approach. The recursive function explores all possible choices of adding open and closed parentheses while keeping track of the counts. It terminates when a valid combination of parentheses with the desired length is reached. The use of the res list allows storing all the valid combinations.
