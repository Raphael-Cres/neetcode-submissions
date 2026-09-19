class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_u = 0
        L = []
        for i in nums:
            if i not in L:
                L.append(i)
                count_u+=1
        
        if count_u != len(nums):
            return True
        else:
            return False
    
        