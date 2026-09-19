class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:    
            max_L = 1
            num_set = set(nums)

            for n in num_set:
                if (n-1) not in num_set:
                    S = 1
                    while n + S in num_set:
                        S += 1

                    if S > max_L:
                        max_L = S

            return max_L


            