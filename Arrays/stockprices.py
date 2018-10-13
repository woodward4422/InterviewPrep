# Question:Say you have an array for which the ith element is the price of a given stock on day i.Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# My initial thoughts are that we need to look to see what adjacent values profits are. We can itierate through the array and subtract the neighbor from the current item and store the highest profit each time with conditionals

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        largest_profit = 0
        buy_date = 0 
        sell_date = 0 
        if not prices or len(prices) == 0:
            return 0 
        for i in range(prices):
            if prices[i+1]: 
                if prices[stock]


