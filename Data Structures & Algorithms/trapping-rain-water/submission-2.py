class Solution:
   
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        left_max = height[left]
        right_max = height[right]
        
        area = 0
        
        while left < right:
            # On se fie toujours au côté qui a le plus petit mur maximum.
            # C'est lui qui dicte la limite de l'eau.
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                # L'eau piégée est la différence entre le plus haut mur à gauche et le mur actuel
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                # L'eau piégée est la différence entre le plus haut mur à droite et le mur actuel
                area += right_max - height[right]
                
        return area