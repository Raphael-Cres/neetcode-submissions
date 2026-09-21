class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        k_min = 1
        k_max = piles[-1]
        n = len(piles)

        def time_eating(k):
            S = 0
            for i in range(n):
                if piles[i]//k == piles[i]/k:
                    S+= (piles[i]//k)
                else:
                    S+= (piles[i]//k) + 1
                

            return S
       
        while k_min<= k_max:
            k_middle = (k_min + k_max)//2
            S = time_eating(k_middle)
            print(S)
            if S <= h:
                k_max = k_middle -1
            if S > h:
                k_min = k_middle + 1

        return k_min


    
