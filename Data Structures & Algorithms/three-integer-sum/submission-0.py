class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(0, n):
            map = {}
            target = -nums[i]
            for j in range(i+1, n):
                if (target - nums[j]) in map:
                    res.add(tuple(sorted([nums[i], nums[j], nums[map[target - nums[j]]]])))
                map[nums[j]] = j

        return list(res)
