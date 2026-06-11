class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low, high
        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] >= pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[low], arr[j] = arr[j], arr[low]
        return j
        
    def quickSort(self, arr, low, high):
        if low < high:
            p_index = self.partition(arr,low, high)
            self.quickSort(arr, low, p_index -1)
            self.quickSort(arr, p_index + 1, high)
