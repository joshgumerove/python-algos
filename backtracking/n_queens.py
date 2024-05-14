class NQueens():
    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]
        
    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print(" Q ", end='')
                else:
                    print(" - ", end='')
            print("\n")
            
    def is_safe_place(self, row_index, col_index):
        for i in range(self.n): # checks horizontally
            if self.chess_table[row_index][i]:
                return False
        j = col_index
        for i in range(row_index, -1, -1): # top left to bottom right
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
            
        j = col_index
        for i in range(row_index, self.n): # top right to bottom left
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j = j - 1
        
        return True
            
    
        

queens = NQueens(4)
queens.print_queens()

