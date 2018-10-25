"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        """ Using BFS idea to loop over the current level""' 
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        from collections import deque
        tree, tQueue, curr, flag=[],deque([root]),[],1
        while tQueue:
            for i in xrange(len(tQueue)):
                # set it to be BFS, go over all the nodes in curr_level
                node=tQueue.popleft()
                curr+=[node.val]
                if node.left:
                    tQueue.append(node.left)
                if node.right:
                    tQueue.append(node.right)
            tree+=[curr[::flag]]
            flag*=-1
            curr=[]
        return tree
            
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    print  Solution().zigzagLevelOrder(n1)       
        
