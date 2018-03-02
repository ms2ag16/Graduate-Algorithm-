# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack=[(p,q)]
        while stack:
            node1,node2=stack.pop()
            if not node1 and not node2: # if node1 is not None and node2 is not None
                continue
            elif None in [node1,node2]:
                return False
            else:
                if node1.val!=node2.val:
                    return False
                stack.append((node1.right,node2.right))
                stack.append((node1.left,node2.left))
        return True

if __name__=="__main__":
    p=TreeNode(2)
    p.left=TreeNode(3)


    q=TreeNode(2)
    q.left=TreeNode(3)


    Solved=Solution()
    print Solved.isSameTree(p,q)
