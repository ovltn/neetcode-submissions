class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        prefix = [0 for _ in range(n)]
        currentMax = height[0]
        for i in range(1, n):
            currentMax = max(currentMax, height[i-1]) 
            prefix[i] = currentMax

        suffix = [0 for _ in range(n)]
        currentMax = height[-1]
        for i in range(n-2, -1, -1):
            currentMax = max(currentMax, height[i+1])
            suffix[i] = currentMax

        res = 0
        for i in range(n):
            if prefix[i] <= height[i] or suffix[i] <= height[i]:
                continue

            res += min(prefix[i], suffix[i]) - height[i]

        return res
