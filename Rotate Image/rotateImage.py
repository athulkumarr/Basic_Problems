def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Rotate the matrix along the principal diagonal
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Rotate the matrix along the middle column
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
            
