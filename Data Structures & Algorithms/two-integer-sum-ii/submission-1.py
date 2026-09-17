class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n-1):
            l, r = i+1, n-1
            while l <= r:
                j = l + (r - l) // 2
                if numbers[j] < target - numbers[i]:
                    l = j+1
                elif numbers[j] > target - numbers[i]:
                    r = j-1
                else:
                    return [i+1, j+1]

        return [0, 0]
