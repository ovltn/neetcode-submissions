class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)

        l, r = 0, 0
        maxF = 0
        res = 0

        while r < len(s):
            counter[s[r]] += 1
            maxF = max(maxF, counter[s[r]])

            while (r-l+1) - maxF > k:
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
            r += 1

        return res