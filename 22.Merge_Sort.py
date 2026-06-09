class Solution:
    def merge_array(self, left, right):
        res = []
        i, j = 0, 0
        n, m = len(left), len(right)
        while i < n and j < m:
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < n:
            while i < n:
                res.append(left[i])
                i += 1
        if j < m:
            while j < m:
                res.append(right[j])
                j += 1
        return res
        
    def mergeSort(self, arr, l=None, r=None): 
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        left_half = self.mergeSort(left_arr)   
        right_half = self.mergeSort(right_arr)
        
        sorted_arr = self.merge_array(left_half, right_half)
        if l is not None:            
            for i in range(len(sorted_arr)):
                arr[i] = sorted_arr[i]
        return sorted_arr
