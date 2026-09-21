class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [x for sublist in matrix for x in sublist]
        n = len(nums)
        a = 0
        b = n-1
        
        while a <=b:
            middle = (b+a)//2
            if nums[middle] == target:
                return True
            elif nums[middle] > target:
                b = middle -1
            elif nums[middle] < target:
                a = middle + 1

        return False
