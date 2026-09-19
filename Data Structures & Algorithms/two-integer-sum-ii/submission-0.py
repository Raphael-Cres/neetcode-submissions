class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n-1
        S = 2 * numbers[right]+ 1
        while S != target:
            S = numbers[left] + numbers[right]
            if S > target:
                right -= 1
            elif S < target:
                left +=1

            else:
                return [left+1, right+1]