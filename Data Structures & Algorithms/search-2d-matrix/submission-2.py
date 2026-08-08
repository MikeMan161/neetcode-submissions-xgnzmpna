class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # define variables
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = (m*n) - 1

        # Binary Search Loop
        while left <= right:
            #calculate mid
            mid = left + (right - left) // 2
            #calculate row and col
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                right = mid - 1
            elif target > matrix[row][col]:
                left = mid + 1
        return False
