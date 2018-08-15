"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if abs(self.maxDepth(root.left)-self.maxDepth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


if __name__ == "__main__":
    n1 = TreeNode(0)
    n2 = TreeNode(-3)
    n3 = TreeNode(9)
    n4 = TreeNode(-10)
    n5 = TreeNode(5)
    n1.right = n3
    n1.left = n2
    n2.left=n4
    n3.left=n5
    print  Solution().isBalanced(n1)
            
        




if __name__ == "__main__":
    n1 = TreeNode(0)
    n2 = TreeNode(-3)
    n3 = TreeNode(9)
    n4 = TreeNode(-10)
    n5 = TreeNode(5)
    n1.right = n3
    n1.left = n2
    n2.left=n4
    n3.left=n5
    print  Solution().isBalanced(n1)
