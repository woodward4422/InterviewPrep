# Question:Say you have an array for which the ith element is the price of a given stock on day i.Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# My initial thoughts are that we need to look to see what adjacent values profits are. We can itierate through the array and subtract the neighbor from the current item and store the highest profit each time with conditionals

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        largest_profit = 0
        #These arent used but I think its a good novelty to have for another question that could be similiar if you want to know both the price to buy and the price to sell
        buy_price = 0 
        sell_price = 0 
        if not prices or len(prices) == 0:
            return 0 
        for i in range(len(prices)):
            for j in range(i+1,len(prices)): 
                current_profit = prices[j] - prices[i]
                if current_profit > largest_profit:
                    largest_profit = current_profit
                    buy_price = prices[i]
                    sell_price = prices[j]
        return largest_profit

solution = Solution()
prices = [1,5,6,1,9,7,8]
profit =solution.maxProfit(prices)
print(profit)

# Final Thoughts: I wasnt too pleased with the run time performance here being O(n^2). I definately think that I could do better than this and will revisit it next time to look for performance enhancements.



                


