class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        return (n & (n - 1)) != 0
        
        
        # for i in range(1, n):
        #     s = 0
        #     num = i
        #     while s < n:
        #         s += num
        #         num += 1
        #         if s == n and num - i >= 2:
        #             return True
        # return False
