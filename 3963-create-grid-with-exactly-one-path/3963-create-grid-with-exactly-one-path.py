class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#"] * n for _ in range(m)]
        i = 0
        j = 0
        grid[0][0] = "."
        while j + 1 < n:
                 
            j += 1
            grid[i][j] = "."
        while i + 1 < m :
            i += 1
            grid[i][j] = "."
        ans = []
        for row in grid:
            ans.append("".join(row))
        return ans 
                

        