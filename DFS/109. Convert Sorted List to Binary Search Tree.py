# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.sortedArrayToBST(array)
    
    def sortedArrayToBST(self, num):
        if not num:
            return None
        midVal = len(num)//2
        root = TreeNode(num[midVal])
        root.left=self.sortedArrayToBST(num[:midVal])
        root.right=self.sortedArrayToBST(num[midVal+1:])
        return root
