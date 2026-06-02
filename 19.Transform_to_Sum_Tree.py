''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        def solve(node):
            if not node:
                return 0
            val = node.data
            left = solve(node.left)
            right = solve(node.right)
            node.data = left + right
            return val + node.data
        solve(root)
