class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m =0
        n = len(heights)
        left = 0
        right = n - 1

        while left < right:
            area = 0
            hl = heights[left]
            hr = heights[right]
            if hl > hr:
                area = hr*(right - left)
                print(area)
                right -=1
            elif hl < hr:
                area = hl*(right - left)
                print(area)
                left += 1
            else:
                area = hl * (right - left)
                while heights[left] == hl and left < right:
                    left+=1
                while heights[right] == hr and left < right:
                    right -=1

            if area > m:
                m = area

        return m
            
            