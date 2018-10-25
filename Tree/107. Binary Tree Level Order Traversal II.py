"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

BFS queue: FIFO
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        tree, curr, bfs=[],[],deque([root])
        while bfs:
            for i in xrange(len(bfs)):
                node=bfs.popleft()
                curr.append(node.val)
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)
            tree.insert(0,curr)
            curr=[]
        return tree

                             
