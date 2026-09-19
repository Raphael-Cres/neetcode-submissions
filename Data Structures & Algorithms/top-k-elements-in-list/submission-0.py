from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        
 
        most_common_elements = freq.most_common(k)
        
        result = [item[0] for item in most_common_elements]
        
        return result