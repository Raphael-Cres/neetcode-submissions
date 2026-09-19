
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(l2):
            return l2[0]**2 + l2[1]**2

        points.sort(key = dist)
        return points[:k]
            
         