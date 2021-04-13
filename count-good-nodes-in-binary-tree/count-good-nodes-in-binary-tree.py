# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # recursive dfs search with state to check 
        def dfs(root, max_sofar):
            
            # the node does not exist so does not contribute to the total good nodes in the tree
            if not root:
                return 0
            
            # initialize total good nodes for this tree
            total = 0
            
            # if the value is greatest we've seen then it's a good node
            # add it to the total and make it the max so far
            if root.val >= max_sofar:
                total += 1
                max_sofar = root.val
                
            # run this procedure on the node's children
            # comparing the children to either the node's value (if it's the max so far) or 
            total += dfs(root.left, max_sofar) # max_sofar for child node is the larger of previous max and current node val
            total += dfs(root.right, max_sofar)

            return total

        # start max_sofar with smallest number possible so any value root has is smaller than it
        return dfs(root, -float('inf'))