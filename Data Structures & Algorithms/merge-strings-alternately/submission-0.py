class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        

        L = []
        m = min(n1,n2)
        
        for i in range(m):
            L.append(word1[i])
            L.append(word2[i])

        if n1 > n2:
            L.append(word1[m:]) 
        elif n2 > n1:
            L.append(word2[m:])

        r = "".join(L)

        return r