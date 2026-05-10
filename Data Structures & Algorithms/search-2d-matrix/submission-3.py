class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1
        search_row_idx = 0

        while top<=bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][0]:
                if target > matrix[mid][right]:
                    top = mid + 1
                else: 
                    search_row_idx = mid
                    break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                return True

        search_row = matrix[search_row_idx]

        while left <= right:
            mid = (left + right) // 2
            if target > search_row[mid]:
                left = mid + 1
            elif target < search_row[mid]:
                right = mid -1
            else:
                return True

        return False


