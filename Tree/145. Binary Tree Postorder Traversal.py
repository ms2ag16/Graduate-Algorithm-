"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
"""



class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """ interatively """
        if not root:
            return []
        result=[]
        """ stack - FILO"""
        stack=[(root,'v')]
        while stack:
            node, label=stack.pop()
            if label=='v':
                stack.append((node,'g'))
                if node.right:
                    stack.append((node.right, 'v'))
                if node.left:
                    stack.append((node.left, 'v'))
            else:
                result.append(node.val)
        return result          
