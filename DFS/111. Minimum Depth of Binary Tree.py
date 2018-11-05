# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
""" iteration version """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack=[root]
        curr=1
        if not root:
            return 0
        while stack:
            for i in range(len(stack)):
                top=stack.pop(0)
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
                if not top.right and not top.left:
                    return curr
            curr+=1
        return curr
    
""" recursion version """
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
        
    
    def dfs(self, root):
        if not root:
            return 0
        if root.left is None:
            return self.dfs(root.right)+1
        if root.right is None:
            return self.dfs(root.left)+1
        return min(self.dfs(root.left), self.dfs(root.right))+1

    
