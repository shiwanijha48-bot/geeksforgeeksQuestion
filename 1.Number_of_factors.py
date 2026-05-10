class Solution:
    def countFactors (self, n):
        # code here
        count = 0
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                count += 1
        return count + 1
# -----------------------------------------
class Solution:
    def countFactors(self, N):
        count = 0
        i = 1
        while i * i <= N:
            if N % i == 0:
                if i == N // i:
                    count += 1  
                else:
                    count += 2  
            i += 1
        return count
