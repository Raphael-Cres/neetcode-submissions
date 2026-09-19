class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1] * n

        PG = 1
        PD = 1

        for i in range(n):
            output[i] = PG
            PG *= nums[i]

        for i in range(n-1,-1,-1):
            output[i] *= PD
            PD *=nums[i]

        return output

        
