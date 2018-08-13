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


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        tree=[]
        if not tree:
            return tree
        curr_level=[root]
        direction='L'
        while curr_level:
            level_list=[]
            next_list=[]
            for temp in curr_level:
                level_list.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.next:
                    next_level.append(temp.right)
            if direction=='L':
                tree.append(level_list)
                direction='R'
            else:
                tree.append(level_list[::-1]
                direction='L'
            curr_level=next_level
        return tree
        
                
           
        
