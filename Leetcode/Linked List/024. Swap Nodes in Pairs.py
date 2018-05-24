""" 
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""




# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=point=ListNode(0)
        dummy.next=head
        while point.next and point.next.next:
      
            tmp=point.next.next 
        
            point.next.next=tmp.next
      
            tmp.next=point.next
       
            point.next=tmp
            point=point.next.next
     return dummy.next
