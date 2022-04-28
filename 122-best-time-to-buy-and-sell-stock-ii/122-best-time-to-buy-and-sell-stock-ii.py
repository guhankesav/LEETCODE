class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        meh = 0
        msf = 0

        for i in range(len(prices)-1):
            meh = prices[i+1] - prices[i]
            if meh > 0:
                msf += meh
            elif meh < 0:
                meh = 0
        return msf