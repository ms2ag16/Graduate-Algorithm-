"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder=preorder
        self.inorder=inorder
        return self._buildTree(0,len(preorder),0,len(inorder))

    def _buildTree(self, pre_start,pre_end,in_start,in_end):
        if pre_start>=pre_end:
            return None
        root=TreeNode(self.preorder[pre_start])
        offset=self.inorder[in_start:in_end+1].index(root.val)
        root.left=self._buildTree(pre_start+1, pre_start+offset+1, in_start, in_start+offset)
        root.right=self._buildTree(pre_start+offset+1, pre_end, in_start+offset+1,in_end)
        return root
        
