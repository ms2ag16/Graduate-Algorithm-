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
        res=[]
        queue=[(root,0)] # start from depth=0
        while len(queue):
            node, depth=queue.pop()
            if node:
                if len(res)<=depth:
                    res.insert(0,[])
                res[-(depth+1)].append(node.val)
                queue.insert(0, (node.left, depth+1)
                queue.insert(0, (node.right, depth+1)
       return res
        
class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        stack=[(root,0)]
        while len(stack)>0:
            node,depth=stack.pop()
            if node:
                if len(res)<=depth:
                    res.insert(0,[])
                res[(-(depth+1))].append(node.val)
                stack.append(node.right,depth+1)
                stack.append(node.left,depth+1)
        return res

                             
