class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        b = True
        left = 0
        right = n-1
        while left < right:
            if not s[left].isalnum():
                left +=1
            elif not s[right].isalnum():
                right -=1
            else:
                if s[left].lower() != s[right].lower():
                    b = False

                left +=1
                right -= 1

        
        return b

        