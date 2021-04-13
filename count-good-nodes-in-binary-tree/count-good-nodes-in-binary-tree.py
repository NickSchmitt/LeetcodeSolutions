# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # recursive dfs with state to compare node val to max ancestor val
        def dfs(root, max_ancestor):
            
            # if the node does not exist it cannot be a good node
            if not root:
                return 0
            
            # initialize total good nodes for this node and its descendents
            total = 0
            
            # if the node's value is greater than the max value of its ancestors
            # add it to the total
            # make it the max ancestor for its descendents
            if root.val >= max_ancestor:
                total += 1
                max_ancestor = root.val
                
            # run this procedure on the node's descendents
            # add their totals to the node's to find the total good nodes
            total += dfs(root.left, max_ancestor)
            total += dfs(root.right, max_ancestor)

            return total

        # start max_ancestor with smallest number possible so any value root has is smaller than it
        return dfs(root, -float('inf'))