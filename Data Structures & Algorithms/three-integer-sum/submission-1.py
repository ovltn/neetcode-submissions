class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        n = len(sNums)
        res = set()

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                current = sNums[j] + sNums[k]

                if current < -sNums[i]:
                    j += 1
                elif current > -sNums[i]:
                    k -= 1
                else:
                    res.add((sNums[i], sNums[j], sNums[k]))
                    j += 1
                    k -= 1

        return [list(x) for x in res]