class Solution:
    def printNos(self, n):
        # Code here
        if n == 0:
            return 
        print(n, end = " ")
        return self.printNos(n-1)
