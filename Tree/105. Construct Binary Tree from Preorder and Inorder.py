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
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        rootIdx = inorder.index(root_val)
        # print (preorder) preorder is shrinking
        root.left = self.buildTree(preorder, inorder[:rootIdx])
        root.right = self.buildTree(preorder, inorder[rootIdx + 1:])
        return root

if __name__=="__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print (Solution().buildTree(preorder,inorder))

