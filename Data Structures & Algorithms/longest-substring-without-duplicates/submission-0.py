class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        l, r = 0, 0
        n = len(s)
        res = 0

        while r < n:
            if not counter[s[r]]:
                counter[s[r]] += 1
                r += 1
            else:
                counter[s[l]] -= 1
                l += 1

            res = max(res, r-l)

        return res
