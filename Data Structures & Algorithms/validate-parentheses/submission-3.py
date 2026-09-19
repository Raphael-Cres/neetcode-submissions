class Solution:
    
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in mapping:
                stack.append(char)
            if char in mapping:
                m = stack.pop() if stack else '3615' 
                if m != mapping[char]:
                    return False
            
                    

        return not stack