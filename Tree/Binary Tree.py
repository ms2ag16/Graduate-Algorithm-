"""
Non-Recursion- preorder
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[root]
        preorder=[]
        if not root:
            return preorder
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder=[]
        stack=[]
        curt = root
        while curt or stack:
            while curt:
                stack.append(curt)
                curt=curt.left
            if stack:
                curt=stack.pop()
                inorder.append(curt.val)
                curt=curt.right
        return inorder


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder=[]
        stack=[root]
        prev = TreeNode(None)
        curr = root

        if not root:
            return None
        while stack:
            curr = stack.pop()
            if not prev or not prev.left or not prev.right: # traverse down the tree
                if curr.left:
                    stack.append(curr.left)
                elif curr.right:
                    stack.append(curr.right)
            elif curr.left == prev: # traverse up the tree from the left
                if curr.right:
                    stack.append(curr.right)
            else:   # traverse up the tree from the right
                postorder.append(curr.val)
            prev = curr
        return postorder


from Tree import Tree


class BinaryTree(Tree):
    """ An abstract base class representing a binary structure. """

    # --- additional abstract methods---------
    def left(self, p):
        """ return a Position representing p's left child,
        return None if p does not have a left child. """
        raise NotImplementedError(' must be implemented by subclass ')

    def right(self, p):
        """ return a Position representing p's right child,
        return None if p does not have a right child. """
        raise NotImplementedError(' must be implemented by subclass ')

    # ---------- concrete method implemented in this class --------
    def sibling(self, p):
        """ return a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """ generate an iteration of Position representing p's children. """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
