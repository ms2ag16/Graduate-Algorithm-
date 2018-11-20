"""
Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

""" recursive """ 
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myprint(self):
        print(self.val)
        if self.next:
            self.next.myprint()

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
    
    def reverse(node, prev=None):
        if not node:
            return prev
        curr=node.next
        node.next=prev
        return self.reverse(curr, node)
        
""" iterative """
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev
        

if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    result = Solution().reverseList(l1)
    result.myprint()
