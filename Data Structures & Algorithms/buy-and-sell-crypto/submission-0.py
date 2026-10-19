class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Tprofit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    profit = prices[j] - prices[i]
                    Tprofit = max(Tprofit, profit)           
        return Tprofit