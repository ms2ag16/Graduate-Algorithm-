"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth, curr_level=0,[root]
        while curr_level:
            depth+=1
            next_level=[]
            for node in curr_level:
                left, right=node.left, node.right
                if left is None and right is None:
                    return depth
                if left:
                    next_level.append(left)
                if right:
                    next_level.append(right)
                curr_level=next_level
        return depth
 
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
    print  Solution().minDepth(n1)
