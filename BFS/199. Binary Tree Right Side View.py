# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        que, curr, res=deque([root]),[],[]
        while que:
            for i in range(len(que)):
                top=que.popleft()
                curr.append(top.val)
                if top.left: que.append(top.left)
                if top.right: que.append(top.right)
            res.append(curr[-1])
        return res
