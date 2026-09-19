class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        pointer_l = 0
        pointer_r = n-1

        while pointer_l < pointer_r:
            a = s[pointer_l]
            s[pointer_l] = s[pointer_r]
            s[pointer_r] = a
            pointer_l+=1
            pointer_r -=1

        