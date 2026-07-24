class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        data: list[int] = [0] * 101
        if n: data[1] = 1
        for i in range(1, n + 1):
            if 2 * i <= n: data[2 * i] = data[i]
            if 2 * i + 1 <= n: data[2 * i + 1] = data[i] + (data[i + 1] if i + 1 < n else 0)
        return max(data)