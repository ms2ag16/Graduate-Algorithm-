"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """ iteratively """
        if not root:
            return []
        queue, res=[root],[]
        while queue:
            n=len(queue)
            while n>0:
                node = queue.pop()
                if node.left:
                    queue.insert(0,node.left)
                if node.right:
                    queue.insert(0, node.right)
                if n==1:
                    res.append(node.val)
                n-=1
        return res


if __name__=="__main__":
    n1=TreeNode(1)
    n2=TreeNode(2)
    n3=TreeNode(3)
    n4=TreeNode(4)
    n5=TreeNode(5)
    n6=TreeNode(6)
    n1.left=n2
    n1.right=n5
    n2.left=n3
    n2.right=n4
    n5.right=n6
    print Solution().rightSideView(n1)
