class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        G = 0
        for i in range(n-1):
            ori = prices[i]
            L = prices[i+1:]
            L.sort()
            m = L[-1] - prices[i]
            if m > G:
                G = m


        return G



        