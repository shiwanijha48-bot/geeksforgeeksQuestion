#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		l -= 1 
        r -= 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr
