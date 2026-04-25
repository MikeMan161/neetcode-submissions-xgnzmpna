class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        "this list comprehension makes each variable a list of sets"
        for r in range(9):
	        for c in range(9):
                 if board[r][c] == ".":
                    continue
                 if board[r][c] in rows[r]:
                    return False
                 else:
                    rows[r].add(board[r][c])
                 if board[r][c] in columns[c]:
                    return False
                 else:
                    columns[c].add(board[r][c])      
                 if board[r][c] in boxes[((r//3)*3)+(c//3)]:
                    return False
                 else:
                    boxes[((r//3)*3)+(c//3)].add(board[r][c])
        return True