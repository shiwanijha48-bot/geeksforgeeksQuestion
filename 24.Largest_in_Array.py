class Solution:
    def largest(self, arr):
        # code here
        maxi = float('-inf') # arr[0]  
        n = len(arr)
        for i in range(0, n):
            maxi = max(arr[i],maxi)
        return maxi
