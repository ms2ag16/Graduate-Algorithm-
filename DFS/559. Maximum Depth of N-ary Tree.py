"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

""" dfs, loop for the child of root children and get the max height
    when loop over child, go deep first to check if it has children and if it does, recursive 
    check, if not return 1 and go check next child of it's parent 
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth=0
        que=[root]
        while que:
            length=len(que)
            for i in range(length):
                top=que.pop(0)
                for child in top.children:
                    que.append(child)
            depth+=1
        return depth


