class Solution:
    def maxProfit(self,prices):
        max_number = 0
        current_max = 0

        for num in reversed(prices):
            current_max = max(current_max, num)              
            # get max result of sub 
            max_number = max(max_number, current_max - num)  # 0  0   3   2   5   0
        
        max_number = 0 if max_number < 0 else max_number
        return max_number 
    
prices = [7,1,5,3,6,4]
o=Solution().maxProfit(prices)          
print(o)


# Less loops and lists for memory

# The function maxProfit takes a list of prices as input.

# The variables max_number and current_max are initialized to 0. max_number will store the maximum profit, and current_max will keep track of the maximum price encountered so far.

# Enter a loop that iterates over the prices in reverse order using the reversed function. This is done to determine the maximum profit that can be obtained by selling at a given price.

# Inside the loop, the code updates current_max to be the maximum value between the current price (num) and the previous current_max value. This ensures that current_max always holds the maximum price encountered so far.

# Then calculates the potential profit that can be obtained by selling at the current price (current_max - num).

# The max_number is updated to be the maximum value between the previous max_number and the potential profit calculated in step 5. This ensures that max_number always holds the maximum profit encountered so far.

# After the loop finishes, the code checks if max_number is less than 0. If it is, it means that no profit can be obtained, so max_number is set to 0.

# Finally, the max_number is returned as the maximum profit that can be obtained from buying and selling the stocks.

# The algorithm used in this code is a simple approach to find the maximum profit. By iterating over the prices in reverse order, it keeps track of the maximum price encountered so far using current_max. It then calculates the potential profit at each price and updates max_number to hold the maximum profit encountered so far.
