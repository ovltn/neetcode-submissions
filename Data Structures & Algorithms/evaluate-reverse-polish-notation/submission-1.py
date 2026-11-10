class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        st = []

        for t in tokens:
            if t in operators:
                b = st.pop()
                a = st.pop()

                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(a-b)
                elif t == '*':
                    st.append(a*b)
                else:
                    st.append(int(a/b))

            else:
                st.append(int(t))

        return st[-1]
