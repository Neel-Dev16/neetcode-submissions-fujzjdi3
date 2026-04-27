class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        res=0
        for price in prices:
            if price<min_price:
                min_price=price
            profit=price-min_price
            res=max(res,profit)
        return res