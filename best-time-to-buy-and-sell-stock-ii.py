#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        full = 0
        for i in range(len(prices)-1):
            if(prices[i+1]-prices[i]>0):
                full+=prices[i+1]-prices[i]
        return full
        
