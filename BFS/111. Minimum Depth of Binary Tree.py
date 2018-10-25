# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        from collections import deque
        bfs, curr=deque([root]),1
        if not root:
            return 0
        while bfs:   
            for i in range(len(bfs)):
                top=bfs.popleft()
                if top.left: bfs.append(top.left)
                if top.right: bfs.append(top.right)
                if not top.left and not top.right:
                    return curr     
            curr+=1
            
        return curr
