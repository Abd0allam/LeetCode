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


# Less loops and lists i memory