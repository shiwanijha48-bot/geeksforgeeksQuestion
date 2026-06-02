class Solution:
    def coin(self, arr):
        # code here
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] > arr[j]:
                i += 1
            else:
                j -= 1
        return arr[i]
