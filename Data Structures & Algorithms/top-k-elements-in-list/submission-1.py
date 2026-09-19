from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] +=1

        liste = []
        for f in d:
            liste.append([ d[f],f])   

        liste.sort(reverse=True)

        L = []
        for i in range(k):
            L.append(liste[i][1])

        return L
       
