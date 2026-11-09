class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open_brackets = {'(': 1, '[': 2, '{': 3}
        close_brackets = {')': 1, ']': 2, '}': 3}

        for c in s:
            if c in open_brackets:
                st.append(c)
                continue

            if c in close_brackets:
                if st and open_brackets[st[-1]] == close_brackets[c]:
                    st.pop()
                else:
                    return False

        return len(st) == 0
