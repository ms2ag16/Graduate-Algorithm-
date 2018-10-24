# BFS Iterative Solution

class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
class Solution(object): 
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        from collections import deque
        lQueue, rQueue= deque([root.left]), deque([root.right])
        while lQueue and rQueue:
            left=lQueue.pop()
            right=rQueue.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            elif left.val!=right.val:
                return False
            lQueue.append(left.left)
            lQueue.append(left.right)
            rQueue.append(right.right)
            rQueue.append(right.left)
        return len(lQueue)==len(rQueue)
    
