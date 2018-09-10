"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
         res=[]
         p=root
         stack=[]
         while p or stack:
            stack.append(p)
            p=p.left
            if stack:
               p=stack.pop()
               res.append(p.val)
               p=p.right
               
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    assert Solution().inorderTraversal(n1) == [1, 3, 2]            
