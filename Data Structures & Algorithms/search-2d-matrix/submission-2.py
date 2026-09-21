import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        n,m = np.shape(matrix)
        a = 0
        b = m*n-1
        
        while a <=b:
            middle = (b+a)//2
            row = middle // m
            column = middle % m



            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                b = middle -1
            elif matrix[row][column] < target:
                a = middle + 1

        return False
