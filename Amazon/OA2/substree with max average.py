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

    
class Node(object):
    def __init__(self, x, children):
        self.val = x
        self.children = children

class Solution2(object):

    def findSubtree(self, root):
        self.average, self.node = 0, None
        self.helper(root)
        return self.node.val

    def helper(self, root):
        sum, size = 0, 0
        if not root:
            return 0, 0
        if root.children:
            for child in root.children:
                child_sum, child_size = self.helper(child)
                sum += child_sum
                size += child_size

            if self.node is None or sum * 1.0 / size > self.average:
                self.node = root
                self.average = sum * 1.0 / size
                
        else:
            sum = root.val
            size = 1
        return sum, size



if __name__=="__main__":
    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    node5 = Node(5, None)
    node6 = Node(6, None)
    node1.children = [node2, node3, node4]
    node2.children = [node5, node6]
    print Solution2().findSubtree(node1)
