class Solution:
    def replaceElements(self, arr):
        # code here
        n = len(arr)
        temp = arr[:]   # copy original array
        for i in range(n):
            if i == 0:
                arr[0] = temp[0] ^ temp[i + 1]
            elif i == n - 1:   # change if -> elif
                arr[n - 1] = temp[n - 2] ^ temp[n - 1]
            else:
                arr[i] = temp[i - 1] ^ temp[i + 1]
        return arr
