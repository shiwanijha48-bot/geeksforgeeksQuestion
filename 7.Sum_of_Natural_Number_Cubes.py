#User function Template for python3

class Solution:
    def sumOfSeries(self,n):
        #code here
        total = 0
        for i in range(1, n+1):
            total = total + i*i*i
        return total
        
        
        
# formula based sol
# return (n * (n + 1) // 2) ** 2
