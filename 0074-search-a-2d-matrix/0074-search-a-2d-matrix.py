class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row=len(matrix)
        cols=len(matrix[0])
        l=0
        r=row*cols-1
        while l<=r:
            m=(l+r)//2
            row=m//cols
            col=m % cols
            if matrix[row][col]==target:
                return True
            elif matrix[row][col] < target:
                l=m+1
            else:
                r=m-1
        return False
