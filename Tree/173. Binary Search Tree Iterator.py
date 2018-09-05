"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
"""


class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        self._pushleft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        node=self.stack.pop()
        self._pushLeft(node.right)
        return node.val

    def _pushleft(self, node):
        while node:
            self.stack.append(node)
            node=node.left
