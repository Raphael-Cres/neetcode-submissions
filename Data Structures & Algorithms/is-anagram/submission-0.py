class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def count(s):
            d = {}
            for i in s:
                if i not in d:
                    d[i] = 1
                else : 
                    d[i] +=1

            return d

        print(count(s))
        return count(s) == count(t)

        

        