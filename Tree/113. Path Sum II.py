"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        result=[]
        self.dfs(root, sum, [], result)
        return result

    def dfs(self, root, sum, curr_list, result):
        if not root:
            return
        sum-=root.val
        if sum==0 and root.left==root.right==None:
            result.append(curr_list+[root.val])
        if root.left:
            self.dfs(root.left, sum, curr_list+[root.val], result)
        if root.right:
            self.dfs(root.right, sum, curr_list+[root.val], result)






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
    print  Solution().pathSum(n1,-3)
