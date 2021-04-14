class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        create a double ended queue to pop off the root efficiently
        while the queue is not empty
            init sum for  current level
            iterate over the queue
                pop first off the queue
                add val to sum
                if children, put them on the queue
            return the sum of the last level
        """
        q = deque([root])
        
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return level_sum