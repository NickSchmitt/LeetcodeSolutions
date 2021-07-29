# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        from collections import deque
        
        dq = deque()
        dq.append(root)
        
        while(len(dq) > 0):
            arr = []
            for i in range(len(dq)):
                node = dq.popleft()
                
                if node.left: 
                    dq.append(node.left)
                    arr.append(node.left.val)
                else:
                    arr.append(None)
                    
                if node.right:
                    dq.append(node.right)
                    arr.append(node.right.val)
                else:
                    arr.append(None)

            if arr != list(reversed(arr)): return False
        
        return True
    
"""

[1,2,2,null,3,null,3]
"""