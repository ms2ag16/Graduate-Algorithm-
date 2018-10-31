"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Solution1, calculate every depth for every node, it's a waste. Recursion Idea, 2 Recursion, 1st calculate maxDepth of a tree
second, 判断每个节点的两个子树高度差是否小于等于1

Solution2, using dfs idea to calculate 在求出每个节点高度的同时，判断是否是平衡二叉树。 
用DFS来计算高度，若高度差超过1，则返回-1.否则，返回高度。
理论上说，对每个节点的访问应该返回两个值：是否平衡、节点高度，为了节省空间，若用-1表示不平衡的状态则可省去一个变量
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
    

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        if abs(self.maxDepth(root.left)-self.maxDepth(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)!=-1
    
    def dfs(self,root):
        if not root:
            return 0
        left, right=self.dfs(root.left), self.dfs(root.right)
        if left<0 or right<0 or abs(left-right)>1:
            return -1
        return max(left, right)+1
        

if __name__ == "__main__":
    n1 = TreeNode(0)
    n2 = TreeNode(-3)
    n3 = TreeNode(9)
    n4 = TreeNode(-10)
    n5 = TreeNode(5)
    n1.right = n3
    n1.left = n2
    n2.left=n4
    n3.left=n5
    print  Solution().isBalanced(n1)
            

