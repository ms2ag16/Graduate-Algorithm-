"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.
"""

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

    def myPrint(self):
        print(self.val)
        if self.next:
            self.next.myPrint()


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
               :type head: ListNode
               :type n: int
               :rtype: ListNode
               """
        dummy=ListNode(0)
        dummy.next=head
        length=0
        first=head
        while (first):
            length+=1
            first=first.next
        length-=n
        
        first=dummy
        while(length>0):
            length-=1
            first=first.next
        first.next=first.next.next
        return dummy.next
