"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""

class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                pre=root.left
                while pre.right:
                    pre=pre.right
                if root.right:
                    pre.right=root.right
                root.right=root.left
                root.left=None
            root=root.right
            
