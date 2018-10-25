"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        tree, bfs, curr=[],deque([root]),[]
        while bfs:
            for i in xrange(len(bfs)):
                node=bfs.popleft()
                curr.append(node.val)
                if node.left: bfs.append(node.left)
                if node.right: bfs.append(node.right)
            tree+=[curr]
            curr=[]
        return tree


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    print  Solution().levelOrder(n1)
