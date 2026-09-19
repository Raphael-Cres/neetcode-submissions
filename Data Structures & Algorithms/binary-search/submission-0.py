class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ind = -1
        for i in range(len(nums)):
            if nums[i ]== target:
                ind = i

        return ind
        