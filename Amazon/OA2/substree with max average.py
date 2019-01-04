""" 给一棵二叉树，找到有最大平均值的子树。返回子树的根结点。""" 
""" divide and conquer + traversal """
class Solution:
    def findSubtree(self, root):
        self.average, self.node = 0, None
        self.helper(root)
        return self.node
    
    def helper(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        
        sum , size = left_sum + right_sum + root.val, left_size + right_size +1
        
        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size
        
        return sum, size
