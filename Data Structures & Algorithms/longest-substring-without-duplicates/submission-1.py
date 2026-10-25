class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = defaultdict(int)

        res = 0
        l, r = 0, 0

        while r < len(s):
            checker[s[r]] += 1

            while checker[s[r]] > 1:
                checker[s[l]] -= 1
                l += 1
                
            res = max(res, r-l+1)
            r += 1

        return res