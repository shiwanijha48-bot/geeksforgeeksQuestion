class Solution:
    def isProduct(self, arr, target):
        # code here
        ans = set()
        for num in arr:
            if target == 0:
                if num == 0 or 0 in ans:
                    return True
            else:
                if num != 0 and target % num == 0:
                    if target // num in ans:
                        return True
            ans.add(num)
        return False
