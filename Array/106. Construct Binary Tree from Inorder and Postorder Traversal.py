# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.inorder=indorder
        self.postorder=postorder
        return self._buildTree(0,len(inorder))
    
    def _buildTree(self,start,end):
        if start<end:
            root=TreeNode(self.postorder.pop())
            index=self.inorder.index(root.val)
            root.right=self._buildTree(index+1,end)
            root.left=self._buildTree(start, index)
            return root
