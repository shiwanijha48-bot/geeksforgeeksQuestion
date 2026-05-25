class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        st = []
        for num in arr:
            if st and ((st[-1] >= 0 and num < 0) or (st[-1] < 0 and num >= 0)):
                st.pop()
            else:
                st.append(num)
        return st
