class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def count(s):
            d = {}
            for i in s:
                if i not in d:
                    d[i] = 1
                else :
                    d[i] +=1

            return d
        d= count(nums)
        return min(d, key=d.get)


        