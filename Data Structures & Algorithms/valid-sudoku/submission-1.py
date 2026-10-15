class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         row = [set() for _ in range(9)]
         col = [set() for _ in range(9)]
         boxes = [set() for _ in range(9)]

         for r in range(len(board)):
            for c in range(len(board[0])):
               if board[r][c] == ".":
                  continue
               if board[r][c] in row[r]:
                  return False
               else:
                  row[r].add(board[r][c])
               if board[r][c] in col[c]:
                  return False
               else:
                  col[c].add(board[r][c])
               if board[r][c] in boxes[((r//3)*3) + (c // 3)]:
                 return False
               else:
                  boxes[((r//3)*3) + (c // 3)].add(board[r][c]) 
         return True