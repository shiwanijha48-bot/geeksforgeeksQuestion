class Solution:
    def findSmallest(self, arr):
        # code here
        arr.sort()  # sorting the arr
        target = 1  # smallest value that cannot be formed yet
        for i in arr:  # traverse all alements in arr
            if i > target:  # if curr num is greater than target
                break   # target cannot be formed
            else:   # extend reachable sum range
                target += i
        return target  # return smallest missing sum
        
