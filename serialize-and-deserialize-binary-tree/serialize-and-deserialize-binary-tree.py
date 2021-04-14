class Codec:
    
    """
    Serialize:
    — Initialize a holding array.
    — Define a dfs recursive function as:
        — If the node is None, append 'null' to the array and return.
        — Append the node's value to the array.
        — Recurse through the node's left, then right descendents.
    — Call dfs on the tree to fill up the holding array.
    — Cast the array values to strings, join them with spaces then return the serialized binary tree.
    """

    def serialize(self, root):
        
        arr = []
        
        def dfs(root):
            if not root:
                arr.append('null')
                return
            
            arr.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ' '.join(str(val) for val in arr)

        
    """
    Deserialize:
    — Define a dfs recursive function as:
        — Get the next item in the iterator.
        — If the value is 'null', just return to represent emptiness.
        — Create a new Node with the value cast to int.
        — Create left descendents by recursing remaining data, then the same for right.
        — Once backtracked from leaves, return the node to its parent.
    — Split the string into a list, and wrap it in an iterator.
    — Call dfs on this iterator to create the deserialized binary tree, and return it.
    """
    def deserialize(self, data):
        
        def dfs(nodes):
            value = next(nodes)
            if value == 'null': return
            node = TreeNode(int(value))
            node.left = dfs(nodes)
            node.right = dfs(nodes)
            return node
        nodes = iter(data.split())
        return dfs(nodes)