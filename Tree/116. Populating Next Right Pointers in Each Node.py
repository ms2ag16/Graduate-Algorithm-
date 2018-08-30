"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
"""

class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next=None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
          return
        curr_level=[root]
        while curr_level:
            next_level=[]
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            for i in range(len(next_level)-1):
                next_level[i].next=next_level[i+1]
            curr_level=next_level
            
            
        
