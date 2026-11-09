class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        c1 = [0] * 26
        c2 = [0] * 26
        for i in range(n1):
            c1[ord(s1[i]) - ord('a')] += 1
            c2[ord(s2[i]) - ord('a')] += 1

        d = sum(c1[i] == c2[i] for i in range(26))
        for i in range(n1, n2):
            if d == 26:
                return True

            r = ord(s2[i]) - ord('a')
            c2[r] += 1
            if c2[r] == c1[r]:
                d += 1
            elif c2[r] - 1 == c1[r]:
                d -= 1

            l = ord(s2[i-n1]) - ord('a')
            c2[l] -= 1
            if c2[l] == c1[l]:
                d += 1
            elif c2[l] + 1 == c1[l]:
                d -= 1

        return d == 26