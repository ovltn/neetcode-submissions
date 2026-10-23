class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        u = defaultdict(int)
        f = 0
        res = 0

        while r < len(s):
            u[s[r]] += 1
            f = max(f, u[s[r]])

            if (r-l+1) - f > k:
                u[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res