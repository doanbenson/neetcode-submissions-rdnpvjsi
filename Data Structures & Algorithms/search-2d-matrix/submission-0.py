class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # middle will be matrix[mid][mid]
        # l = matrix[0][0], r = matrix[len - 1][len - 1]
        # same algo from there

        flatten_matrix = [item for sublist in matrix for item in sublist]
        l, r = 0, len(flatten_matrix) - 1
        while l <= r:
            mid = (l + r) // 2
            if flatten_matrix[mid] == target:
                return True
            elif flatten_matrix[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return False