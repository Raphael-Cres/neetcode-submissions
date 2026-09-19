class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)

        for i in range(n):
            P = 1
            for j in range(n):
                if j != i:
                    P*= nums[j]
            output.append(round(P))

        return output