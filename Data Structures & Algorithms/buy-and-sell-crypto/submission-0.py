class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxi = 0
        for i in range(n-1):
            L = prices[i:]
            print(prices)
            print(L)
            m = max(L)
            maxi = max(maxi, m- prices[i])

        return maxi


        