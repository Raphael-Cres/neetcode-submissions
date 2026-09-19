class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = max(nums) + 1
        for num in nums:
            single = single ^ num

        return single^ (max(nums) + 1)

        