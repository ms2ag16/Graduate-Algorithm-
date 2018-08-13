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
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        stack=[]
        p=root
        while p or stack:
            # save the node which have left child
            while p:
                stack.append(p)
                p=p.left
            if stack:
                p=stack.pop()
                # visit the (left node, root) 
                result.append(p.val)
                #visit the right subtree
                p=p.right
        return result


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    print  Solution().inorderTraversal(n1)                
                
