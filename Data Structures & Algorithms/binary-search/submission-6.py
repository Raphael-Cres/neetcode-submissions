class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        a = 0
        b = n-1
        
        while a <=b:
            middle = (b+a)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                b = middle -1
            elif nums[middle] < target:
                a = middle + 1

        return -1
