class Solution: 
    def selectionSort(self, arr):
        #code here
        n = len(arr)
        for i in range(0,n):
            mini_ind = i
            for j in range(i + 1, n):
                if arr[j] < arr[mini_ind]:
                    mini_ind = j
            arr[i], arr[mini_ind] = arr[mini_ind], arr[i]
        return arr
        
