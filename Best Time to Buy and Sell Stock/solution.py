class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprofit = 899999
        for i in range(len(prices)):
            if prices[i] < minprofit:
                minprofit = prices[i]
            elif prices[i] > maxprofit:
                maxprofit = prices[i] - minprofit
        return maxprofit
