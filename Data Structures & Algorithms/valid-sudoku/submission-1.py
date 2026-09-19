class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        L_col = [[L[i] for L in board] for i in range(len(board))]

        def detect_duplicate(L: List):
            l = []
            for i in L:
                if i in l:
                    return True
                if i != ".":
                    l.append(i)

            return False

        for j in L_col:
            if detect_duplicate(j):
                return False

        for j in board:
            if detect_duplicate(j):
                return False


        N = len(board)
        n = N//3
        square = []
        i = 1
        

        while i < N :
            j = 1
            while j < N:
                sq = []
                for k in range(i-1,i+2,1):
                    for r in range(j-1,j+2,1):
                        sq.append(board[k][r])

                j+=3
                square.append(sq)
            i+=3

                

        for s in square:
            if detect_duplicate(s):
                return False


        return True



            