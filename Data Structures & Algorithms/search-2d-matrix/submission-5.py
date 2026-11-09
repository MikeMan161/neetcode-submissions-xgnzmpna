class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        best = 0

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[best][mid] == target:
                return True
            elif matrix[best][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False