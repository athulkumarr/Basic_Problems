def minPathSum(self, grid: List[List[int]]) -> int:
    m,n = len(grid), len(grid[0])
    dp = [[float('inf') for i in range(n)]for j in range(m)]

    dp[0][0] = grid[0][0]
    for col in range(1,n):
        dp[0][col] = dp[0][col-1] + grid[0][col]

    for row in range(1,m):
        for col in range(n):
            dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
    print(dp)
    return dp[m-1][n-1]
