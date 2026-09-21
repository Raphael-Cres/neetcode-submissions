
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        m = len(matrix[0])
        n = len(matrix)
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
